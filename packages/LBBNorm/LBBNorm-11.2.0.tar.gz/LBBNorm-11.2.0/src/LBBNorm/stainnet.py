import numpy as np
import torch
from stainnet_dir.models import StainNet
from LBBNorm.src.LBBNorm.image_handler import LoadImages, SaveImages


class StainNet():
    def __init__(self, mode="histopathology"):
        self.model_stainnet = StainNet()
        if mode == "cytopathology":
            self.model_stainnet.load_state_dict(torch.load("./StainNet/checkpoints/aligned_cytopathology_dataset/StainNet-3x0_best_psnr_layer3_ch32.pth", map_location=torch.device('cpu')))
        if mode == "histopathology":
            self.model_stainnet.load_state_dict(torch.load("./StainNet/checkpoints/aligned_histopathology_dataset/StainNet-Public_layer3_ch32.pth", map_location=torch.device('cpu')))
        if mode == "camelyon":
            self.model_stainnet.load_state_dict(torch.load("./StainNet/checkpoints/camelyon16_dataset/StainNet-Public-centerUni_layer3_ch32.pth", map_location=torch.device('cpu')))

    
    def norm(self, image):
        image = image.transpose((2, 0, 1))
        image = ((image / 255) - 0.5) / 0.5
        image=image[np.newaxis, ...]
        image=torch.from_numpy(image)
        return image

    def un_norm(self, image):
        image = image.cpu().detach().numpy()[0]
        image = ((image * 0.5 + 0.5) * 255).astype(np.uint8).transpose((1,2,0))
        return image   
    
    
    def transform(self,X,save_to_file=False,result_dir='./stainnet_result/'):

        images,image_names = LoadImages(X)
        output = []
        for img in images:
            
            image_net=self.model_stainnet(self.norm(img))
            output.append(self.un_norm(image_net))
        if save_to_file:
            SaveImages(output,result_dir)
            print('Output successfully saved in '+ output)
            return True
        else:
            return output