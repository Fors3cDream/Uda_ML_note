"""
Create by Killer at 2019-04-25 16:24
"""

import ast
from PIL import Image
import torchvision.transforms as transforms
from torch.autograd import Variable
import torchvision.models as models
from torch import __version__

resnet18 = models.resnet18(pretrained=True)
alexnet = models.alexnet(pretrained=True)
vgg16 = models.vgg16(pretrained=True)

models = {'resnet': resnet18, 'alexnet': alexnet, 'vgg': vgg16}

# obtain ImageNet labels
with open('imagenet1000_clsid_to_human.txt') as imagenet_classes_file:
    imagenet_classes_dict = ast.literal_eval(imagenet_classes_file.read())


def classifier(img_path, model_name):
    # load the image
    img_pil = Image.open(img_path)

    # define transforms
    preprocess = transforms.Compose([
        transforms.Resize(256),
        transforms.CenterCrop(224),
        transforms.ToTensor(),
        transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225])
    ])

    # preprocess the image
    img_tensor = preprocess(img_pil)

    # resize the tensor (add dimension for batch)
    img_tensor.unsqueeze_(0)

    # wrap input in variable, wrap input in variable - no longer needed for
    # v0.4 & higher code to handle PyTorch upgrade
    pytorch_ver = __version__.split(".")

    if int(pytorch_ver[0]) > 0 or int(pytorch_ver[1]) >= 4:
        img_tensor.requires_grad_(False)

    else:
        data = Variable(img_tensor, volatile=True)

    # apply model to input
    model = models[model_name]

    # puts model in evaluation mode
    # instead of (default)training mode
    model = model.eval()

    if int(pytorch_ver[0])>0 or int(pytorch_ver[1])>=4:
        output = model(img_tensor)
    else:
        output = model(data)

    pred_idx = output.data.numpy().argmax()

    return imagenet_classes_dict[pred_idx]