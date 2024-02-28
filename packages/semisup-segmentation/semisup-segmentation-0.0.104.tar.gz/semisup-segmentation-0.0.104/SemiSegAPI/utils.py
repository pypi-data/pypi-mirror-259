import gc
import glob
import cv2

from fastai.vision.all import *
from fastai.basics import *
from fastai.vision.all import *
from fastai.data.all import *
from semtorch import get_segmentation_learner
import segmentation_models_pytorch as smp

from pathlib import Path
import torch
import PIL
from torchvision import transforms

import importlib
from SemiSegAPI.architectures import DenseASPP
from SemiSegAPI.architectures import CGNet
from SemiSegAPI.architectures import FPENet
from SemiSegAPI.architectures import OCNet
from SemiSegAPI.architectures import LEDNet
from SemiSegAPI.architectures import UNet
from tqdm import tqdm_notebook as tqdm

from albumentations import (
    Compose,
    OneOf,
    ElasticTransform,
    GridDistortion,
    OpticalDistortion,
    Flip,
    HorizontalFlip,
    Rotate,
    Transpose,
    CLAHE,
    ShiftScaleRotate
)


try:
    shell = get_ipython().__class__.__name__
    if shell == 'ZMQInteractiveShell':
        from tqdm import tqdm_notebook as tqdm
    else:
        from tqdm import tqdm
except NameError:
    from tqdm import tqdm

availableModels=['CGNet', 'FPENet', 'DeepLab','PAN','OCNet','MAnet','LEDNet','DenseASPP','U-Net','HRNet']
availableTransforms=['H Flip','V Flip','H+V Flip','Blurring','Gamma','Gaussian Blur','Median Blur','Bilateral Filter','Equalize histogram','2D-Filter']

def testNameModel(model):
    return model in availableModels

def testPath(path):
    return os.path.isdir(path+os.sep+'Images'+os.sep+'train') and os.path.isdir(path+os.sep+'Images'+os.sep+'valid') and os.path.isdir(path+os.sep+'Labels'+os.sep+'train') and os.path.isdir(path+os.sep+'Labels'+os.sep+'valid')

def testTransforms(transforms):
    for transform in transforms:
        if not transform in availableTransforms:
            return False
    return True


def transformImage(image):
    my_transforms = transforms.Compose([transforms.ToTensor(),
                                        transforms.Normalize(
                                            [0.485, 0.456, 0.406],
                                            [0.229, 0.224, 0.225])])
    image_aux = image
    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

    return my_transforms(image_aux).unsqueeze(0).to(device)


def getImageFromOut(output,size,codesFile):
    vocabs=get_codes(codesFile)
    mask = np.array(output.cpu())
    mask2=mask.copy()

    for vocab in vocabs.keys():
        mask2[mask==vocabs[vocab][0]]=vocabs[vocab][1][0]

    mask2=np.reshape(mask2,size)
    return Image.fromarray(mask2.astype('uint8'))

def getTransformReverse(transform, image):
    if transform=="H Flip":
        return cv2.flip(image,0)
    elif transform=="V Flip":
        return cv2.flip(image,1)
    elif transform=="H+V Flip":
        return cv2.flip(image,-1)
    else: return image


def averageVotingEnsemble(predictions):
    softOutput=torch.nn.Softmax(1)
    output=softOutput(predictions[0])
    for l in predictions:
        output=output+softOutput(l)
    output=output-softOutput(predictions[0])
    output=output/len(predictions)
    finalPredictions = torch.max(output,1)
    return finalPredictions


def omniModel(path,models,backbones,size=(480,640)):
    images = sorted(glob.glob(path+os.sep+'unlabeled_images' + os.sep + "*"))
    newPath = path + "_tmp"
    if not os.path.exists(newPath):
        shutil.copytree(path, newPath)
    else:
        raise Exception("The path " + newPath + " already exists")

    predictions = {}
    nClasses = getNumClasses(path)
    for model, backbone in zip(models,backbones):
        dls = get_dls(path, size, bs=1)
        learn = getLearner(model, backbone, nClasses, path, dls)
        device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
        learn.load(model + '_' + backbone,device=device,with_opt=False)
        learn.model.eval()
        learn.model.to(device)
        del dls
        gc.collect()
        torch.cuda.empty_cache()

        print('Processing images with ' + model + ' model')
        for image in tqdm(images):
            name = image.split(os.sep)[-1]
            if name not in predictions:
                predictions[name]=[]
            img = PIL.Image.open(image)
            imag = transforms.Resize(size)(img)
            tensor = transformImage(image=imag)
            p = learn.model(tensor)
            predictions[name].append(p.cpu().detach())
            gc.collect()
            torch.cuda.empty_cache()
        del learn
        gc.collect()
        torch.cuda.empty_cache()

    print('Annotating images')
    for image in tqdm(images):
        name = image.split(os.sep)[-1]
        prob, indices = averageVotingEnsemble(predictions[name])
        newMask = getImageFromOut(indices, size, path + os.sep + 'codes.txt')
        img.save(newPath + os.sep + 'Images' + os.sep + 'train' + os.sep + 'new_' + name)
        newMask.save(newPath + os.sep + 'Labels' + os.sep + 'train' + os.sep + 'new_' + name)
    del predictions
    gc.collect()
    torch.cuda.empty_cache()


def omniData(path, model,backbone, transformations, size=(480,640)):
    dls = get_dls(path, size, bs=1)
    nClasses = getNumClasses(path)
    learn = getLearner(model, backbone, nClasses, path, dls)
    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    learn.load(model + '_' + backbone,device=device,with_opt=False)
    learn.model.eval()
    learn.model.to(device)

    del dls
    gc.collect()
    torch.cuda.empty_cache()

    images = sorted(glob.glob(path+os.sep+'unlabeled_images' + os.sep + "*"))
    newPath = path + "_tmp"
    if not os.path.exists(newPath):
        shutil.copytree(path, newPath)
    else:
        raise Exception("The path " + newPath + " already exists")

    print('Processing images with ' + model + ' model')
    for image in tqdm(images):
        name = image.split(os.sep)[-1]
        img = PIL.Image.open(image)
        imag = transforms.Resize(size)(img)
        tensor = transformImage(image=imag)

        lista = []

        pn = learn.model(tensor)
        lista.append(pn.cpu().detach())

        im = cv2.imread(image, 1)
        im = cv2.cvtColor(im, cv2.COLOR_BGR2RGB)

        for transform in transformations:
            img = getTransform(transform, im)
            img = PIL.Image.fromarray(img)
            imag = transforms.Resize(size)(img)
            tensor = transformImage(image=imag)
            p = learn.model(tensor)
            p = np.asarray(p.cpu().detach())
            p=p[0]
            axis0=p.shape[0]
            for i in range(axis0):
                if i==0:
                    res=np.expand_dims(getTransformReverse(transform, p[i]),axis=0)
                else:
                    res=np.append(res, np.expand_dims(getTransformReverse(transform, p[i]),axis=0), axis=0)
            p=np.expand_dims(res, axis=0)
            lista.append(torch.from_numpy(p).cpu().detach())
            gc.collect()
            torch.cuda.empty_cache()
        prob, indices = averageVotingEnsemble(lista)
        newMask = getImageFromOut(indices,size,path + os.sep + 'codes.txt')

        img.save(newPath + os.sep + 'Images' + os.sep + 'train' + os.sep + 'new_' + name)
        newMask.save(newPath + os.sep + 'Labels' + os.sep + 'train' + os.sep + 'new_' + name)
        gc.collect()
        torch.cuda.empty_cache()
    del learn
    gc.collect()
    torch.cuda.empty_cache()

def omniModelData(path, models, backbones, transformations, size):
    images = sorted(glob.glob(path+os.sep+'unlabeled_images' + os.sep + "*"))
    newPath = path + "_tmp"
    if not os.path.exists(newPath):
        shutil.copytree(path, newPath)
    else:
        raise Exception("The path " + newPath + " already exists")

    predictions = {}
    nClasses = getNumClasses(path)
    for model, backbone in zip(models,backbones):
        dls = get_dls(path, size, bs=1)
        learn = getLearner(model, backbone, nClasses, path, dls)
        device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
        learn.load(model + '_' + backbone,device=device,with_opt=False)
        learn.model.eval()
        learn.model.to(device)
        del dls
        gc.collect()
        torch.cuda.empty_cache()
        print('Processing images with ' + model + ' model')
        for image in tqdm(images):
            name = image.split(os.sep)[-1]
            if name not in predictions:
                predictions[name]=[]
            img = PIL.Image.open(image)
            imag = transforms.Resize(size)(img)
            tensor = transformImage(image=imag)
            pn = learn.model(tensor)
            predictions[name].append(pn.cpu().detach())

            im = cv2.imread(image, 1)
            im = cv2.cvtColor(im, cv2.COLOR_BGR2RGB)
            for transform in transformations:
                img = getTransform(transform, im)
                img = PIL.Image.fromarray(img)
                imag = transforms.Resize(size)(img)
                tensor = transformImage(image=imag)
                p = learn.model(tensor)
                p = np.asarray(p.cpu().detach())
                p = p[0]
                axis0 = p.shape[0]
                for i in range(axis0):
                    if i == 0:
                        res = np.expand_dims(getTransformReverse(transform, p[i]), axis=0)
                    else:
                        res = np.append(res, np.expand_dims(getTransformReverse(transform, p[i]), axis=0), axis=0)
                p = np.expand_dims(res, axis=0)
                predictions[name].append(torch.from_numpy(p).cpu().detach())
            gc.collect()
            torch.cuda.empty_cache()
        del learn
        gc.collect()
        torch.cuda.empty_cache()

    print('Annotating images')
    for image in tqdm(images):
        name = image.split(os.sep)[-1]
        prob, indices = averageVotingEnsemble(predictions[name])
        newMask = getImageFromOut(indices, size, path + os.sep + 'codes.txt')
        img.save(newPath + os.sep + 'Images' + os.sep + 'train' + os.sep + 'new_' + name)
        newMask.save(newPath + os.sep + 'Labels' + os.sep + 'train' + os.sep + 'new_' + name)
    del predictions
    gc.collect()
    torch.cuda.empty_cache()


# Models
def create_denseaspp(backbone,numClasses):
    return DenseASPP(backbone_name=backbone, nclass=numClasses)

def create_deeplab(backbone,numClasses):
    model = smp.Unet(
        encoder_name=backbone,  # choose encoder, e.g. mobilenet_v2 or efficientnet-b7
        encoder_weights="imagenet",  # use `imagenet` pre-trained weights for encoder initialization
        in_channels=4,  # model input channels (1 for gray-scale images, 3 for RGB, etc.)
        classes=3,  # model output channels (number of classes in your dataset)
    )
    return model

def create_cgnet(backbone,numClasses):
    model = CGNet(nclass=numClasses)
    return model


def create_fpenet(backbone,numClasses):
    model = FPENet(nclass=numClasses)
    return model


def create_pan(backbone,numClasses):
    model = smp.PAN(
        encoder_name=backbone,  # choose encoder, e.g. mobilenet_v2 or efficientnet-b7
        encoder_weights="imagenet",  # use `imagenet` pre-trained weights for encoder initialization
        in_channels=3,  # model input channels (1 for gray-scale images, 3 for RGB, etc.)
        classes=numClasses,  # model output channels (number of classes in your dataset)
    )
    return model

def create_ocnet(backbone,numClasses):
    return OCNet(backbone_name=backbone, nclass=numClasses)

def create_manet(backbone,numclasses):
    model = smp.MAnet(
        encoder_name=backbone,  # choose encoder, e.g. mobilenet_v2 or efficientnet-b7
        encoder_weights="imagenet",  # use `imagenet` pre-trained weights for encoder initialization
        in_channels=3,  # model input channels (1 for gray-scale images, 3 for RGB, etc.)
        classes=numclasses,  # model output channels (number of classes in your dataset)
    )
    return model

def create_lednet(backbone,numClasses):
    return LEDNet(nclass=numClasses)

def create_unet(backbone,numClasses):
    return UNet(nclass=numClasses)




def getModel(model,backbone,numClasses):
    modelo='create_'+model.lower()
    method=getattr(importlib.import_module("SemiSegAPI.utils"),modelo)
    return method(backbone,numClasses)




def getLearner(model,backbone,numClasses,path,dls):
    if numClasses > 2:
        metric = [DiceMulti(), JaccardCoeffMulti(), foreground_acc]
        save = SaveModelCallback(monitor='dice_multi', fname=model+'_'+backbone)
        early = EarlyStoppingCallback(monitor='dice_multi', patience=5)
    else:
        metric = [Dice(), JaccardCoeff(), foreground_acc]
        save = SaveModelCallback(monitor='dice', fname=model+'_'+backbone)
        early = EarlyStoppingCallback(monitor='dice', patience=5)
    if model=='U-Net':
        learn = get_segmentation_learner(dls=dls, number_classes=numClasses, segmentation_type="Semantic Segmentation",
                                         architecture_name="unet", backbone_name=backbone,
                                         metrics=metric, wd=1e-2,cbs=[early, save],
                                         pretrained=True, normalize=True, path=path)
    elif model=='DeepLab':
        learn=get_segmentation_learner(dls=dls, number_classes=numClasses, segmentation_type="Semantic Segmentation",
                                 architecture_name="deeplabv3+", backbone_name=backbone,
                                 metrics=metric,wd=1e-2,cbs=[early, save],
                                 pretrained=True,normalize=True,path=path)
    elif model=='HRNet':
        learn=get_segmentation_learner(dls=dls, number_classes=numClasses, segmentation_type="Semantic Segmentation",
                                 architecture_name="hrnet", backbone_name='hrnet_w48',
                                 metrics=metric,wd=1e-2,cbs=[early, save],
                                 pretrained=True,normalize=True,path=path)
    else:
        bModel = getModel(model, backbone, numClasses)
        learn = Learner(dls, bModel, metrics=metric, cbs=[early, save],
                        path=path)
    return learn



def getTransform(transform, image):
    if transform=="H Flip":
        return cv2.flip(image,0)
    elif transform=="V Flip":
        return cv2.flip(image,1)
    elif transform=="H+V Flip":
        return cv2.flip(image,-1)
    elif transform=="Blurring":
        return cv2.blur(image,(5,5))
    elif transform=="Gamma":
        invGamma = 1.0
        table = np.array([((i / 255.0) ** invGamma) * 255 for i in np.arange(0, 256)]).astype('uint8')
        return cv2.LUT(image, table)
    elif transform=="Gaussian Blur":
        return cv2.GaussianBlur(image,(5,5),cv2.BORDER_DEFAULT)
    elif transform=="Median Blur":
        return cv2.medianBlur(image,5)
    elif transform=="Bilateral Filter":
        return cv2.bilateralFilter(image,9,75,75)
    elif transform=="Equalize histogram":
        equ_im = cv2.equalizeHist(image)
        return np.hstack((image, equ_im))
    elif transform=="2D-Filter":
        kernel = np.ones((5, 5), np.float32) / 25
        return cv2.filter2D(image, -1, kernel)

def train_learner(learn,epochs,freeze_epochs=2):
    learn.fit_one_cycle(freeze_epochs)
    learn.unfreeze()
    learn.lr_find(show_plot=False)
    lr=learn.recorder.lrs[np.argmin(learn.recorder.losses)]
    if lr<1e-05:
        lr=1e-03
    learn.fit_one_cycle(epochs,lr_max=slice(lr/100,lr))


get_y_fn = lambda x: Path(str(x).replace("Images","Labels"))


def ParentSplitter(x):
    return Path(x).parent.name=='valid'

def get_dls(path,size=(480, 640),bs=4):
    vocabs=get_codes(path + os.sep + 'codes.txt')
    trainDB = DataBlock(blocks=(ImageBlock, MaskBlock(vocabs.keys())),
                   get_items=partial(get_image_files,folders=['train','valid']),
                   get_y=get_y_fn,
                   splitter=FuncSplitter(ParentSplitter),
                   item_tfms=[Resize(size), TargetMaskConvertTransform(vocabs), transformPipeline()],
                   batch_tfms=Normalize.from_stats(*imagenet_stats)
                  )
    dls = trainDB.dataloaders(path+os.sep+'Images', bs=bs)
    return dls


class SegmentationAlbumentationsTransform(ItemTransform):
    split_idx = 0

    def __init__(self, aug):
        self.aug = aug

    def encodes(self, x):
        img, mask = x
        aug = self.aug(image=np.array(img), mask=np.array(mask))
        return PILImage.create(aug["image"]), PILMask.create(aug["mask"])

def transformPipeline():
    transforms = Compose([
        HorizontalFlip(p=0.5),
        Rotate(p=0.40, limit=10), GridDistortion()
    ], p=1)

    transforms = SegmentationAlbumentationsTransform(transforms)
    return transforms

def getNumClasses(path):
    return np.loadtxt(path +os.sep+ 'codes.txt', dtype=str).size


class TargetMaskConvertTransform(ItemTransform):
    def __init__(self,codes):
        super()
        self.codes=codes

    def encodes(self, x):
        img, mask = x

        # Convert to array
        mask = np.array(mask)
        mask2=mask.copy()
        for code in self.codes.keys():
            for num in self.codes[code][1]:
                mask2[mask == num] = self.codes[code][0]

        # Back to PILMask
        mask = PILMask.create(mask2)
        return img, mask

def get_codes(codes):
    vocabs={}
    fichero=open(codes)
    lineas=fichero.readlines()
    for i,linea in enumerate(lineas):
        cont=linea.split(',')
        vocab=cont[0]
        vocabs[vocab]=[i,[int(i) for i in cont[1:]]]
    return vocabs