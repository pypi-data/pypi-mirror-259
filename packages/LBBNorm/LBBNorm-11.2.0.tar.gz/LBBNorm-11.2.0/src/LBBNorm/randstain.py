
from .image_handler import LoadImages,SaveImages
import os
import cv2
import numpy as np
import yaml
import random
from skimage import color
from fitter import Fitter
from typing import Optional, Dict


class Dict2Class(object):
    # ToDo: Wrap into RandStainNA
    def __init__(self, my_dict: Dict):
        self.my_dict = my_dict
        for key in my_dict:
            setattr(self, key, my_dict[key])

def get_yaml_data(yaml_file):
    # ToDo: Wrap into RandStainNA
    file = open(yaml_file, "r", encoding="utf-8")
    file_data = file.read()
    file.close()
    # str->dict
    data = yaml.load(file_data, Loader=yaml.FullLoader)

    return data

class RandStainNAAdaptor(object):
    # ToDo: support downloading yaml file from online if the path is not provided.
    def __init__(
        self,
        yaml_file: str,
        std_hyper: Optional[float] = 0,
        distribution: Optional[str] = "normal",
        probability: Optional[float] = 1.0,
        is_train: Optional[bool] = True,
    ):

        # true:training setting/false: demo setting

        assert distribution in [
            "normal",
            "laplace",
            "uniform",
        ], "Unsupported distribution style {}.".format(distribution)

        self.yaml_file = yaml_file
        cfg = get_yaml_data(self.yaml_file)
        c_s = cfg["color_space"]

        self._channel_avgs = {
            "avg": [
                cfg[c_s[0]]["avg"]["mean"],
                cfg[c_s[1]]["avg"]["mean"],
                cfg[c_s[2]]["avg"]["mean"],
            ],
            "std": [
                cfg[c_s[0]]["avg"]["std"],
                cfg[c_s[1]]["avg"]["std"],
                cfg[c_s[2]]["avg"]["std"],
            ],
        }
        self._channel_stds = {
            "avg": [
                cfg[c_s[0]]["std"]["mean"],
                cfg[c_s[1]]["std"]["mean"],
                cfg[c_s[2]]["std"]["mean"],
            ],
            "std": [
                cfg[c_s[0]]["std"]["std"],
                cfg[c_s[1]]["std"]["std"],
                cfg[c_s[2]]["std"]["std"],
            ],
        }

        self.channel_avgs = Dict2Class(self._channel_avgs)
        self.channel_stds = Dict2Class(self._channel_stds)

        self.color_space = cfg["color_space"]
        self.p = probability
        self.std_adjust = std_hyper
        self.color_space = c_s
        self.distribution = distribution
        self.is_train = is_train

    def _getavgstd(self, image: np.ndarray, isReturnNumpy: Optional[bool] = True):

        avgs = []
        stds = []

        num_of_channel = image.shape[2]
        for idx in range(num_of_channel):
            avgs.append(np.mean(image[:, :, idx]))
            stds.append(np.std(image[:, :, idx]))

        if isReturnNumpy:
            return (np.array(avgs), np.array(stds))
        else:
            return (avgs, stds)

    def _normalize(
        self,
        img: np.ndarray,
        img_avgs: np.ndarray,
        img_stds: np.ndarray,
        tar_avgs: np.ndarray,
        tar_stds: np.ndarray,
    ) -> np.ndarray:

        img_stds = np.clip(img_stds, 0.0001, 255)
        img = (img - img_avgs) * (tar_stds / img_stds) + tar_avgs

        if self.color_space in ["LAB", "HSV"]:
            img = np.clip(img, 0, 255).astype(np.uint8)

        return img

    def augment(self, img):
        # img:is_train:false——>np.array()(cv2.imread()) #BGR
        # img:is_train:True——>PIL.Image #RGB

        if self.is_train == False:
            image = img
        else:
            image = cv2.cvtColor(np.array(img), cv2.COLOR_RGB2BGR)

        num_of_channel = image.shape[2]

        # color space transfer
        if self.color_space == "LAB":
            image = cv2.cvtColor(image, cv2.COLOR_BGR2LAB)
        elif self.color_space == "HSV":
            image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
        elif self.color_space == "HED":
            image = color.rgb2hed(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))

        std_adjust = self.std_adjust

        # virtual template generation
        tar_avgs = []
        tar_stds = []
        if self.distribution == "uniform":

            # three-sigma rule for uniform distribution
            for idx in range(num_of_channel):

                tar_avg = np.random.uniform(
                    low=self.channel_avgs.avg[idx] - 3 * self.channel_avgs.std[idx],
                    high=self.channel_avgs.avg[idx] + 3 * self.channel_avgs.std[idx],
                )
                tar_std = np.random.uniform(
                    low=self.channel_stds.avg[idx] - 3 * self.channel_stds.std[idx],
                    high=self.channel_stds.avg[idx] + 3 * self.channel_stds.std[idx],
                )

                tar_avgs.append(tar_avg)
                tar_stds.append(tar_std)
        else:
            if self.distribution == "normal":
                np_distribution = np.random.normal
            elif self.distribution == "laplace":
                np_distribution = np.random.laplace

            for idx in range(num_of_channel):
                tar_avg = np_distribution(
                    loc=self.channel_avgs.avg[idx],
                    scale=self.channel_avgs.std[idx] * (1 + std_adjust),
                )

                tar_std = np_distribution(
                    loc=self.channel_stds.avg[idx],
                    scale=self.channel_stds.std[idx] * (1 + std_adjust),
                )
                tar_avgs.append(tar_avg)
                tar_stds.append(tar_std)

        tar_avgs = np.array(tar_avgs)
        tar_stds = np.array(tar_stds)

        img_avgs, img_stds = self._getavgstd(image)

        image = self._normalize(
            img=image,
            img_avgs=img_avgs,
            img_stds=img_stds,
            tar_avgs=tar_avgs,
            tar_stds=tar_stds,
        )

        if self.color_space == "LAB":
            image = cv2.cvtColor(image, cv2.COLOR_LAB2BGR)
        elif self.color_space == "HSV":
            image = cv2.cvtColor(image, cv2.COLOR_HSV2BGR)
        elif self.color_space == "HED":
            nimg = color.hed2rgb(image)
            imin = nimg.min()
            imax = nimg.max()
            rsimg = (255 * (nimg - imin) / (imax - imin)).astype(
                "uint8"
            )  # rescale to [0,255]

            image = cv2.cvtColor(rsimg, cv2.COLOR_RGB2BGR)

        return image

    def __call__(self, img):
        if np.random.rand(1) < self.p:
            return self.augment(img)
        else:
            return img

    def __repr__(self):
        format_string = self.__class__.__name__ + "("
        format_string += f"methods=Reinhard"
        format_string += f", colorspace={self.color_space}"
        format_string += f", mean={self._channel_avgs}"
        format_string += f", std={self._channel_stds}"
        format_string += f", std_adjust={self.std_adjust}"
        format_string += f", distribution={self.distribution}"
        format_string += f", p={self.p})"
        return format_string


class RandStainNA():
    
    def __init__(self, dataset_name="RStain"):
        self.dataset_name = dataset_name
    
    def _getavgstd(image):
        avg = []
        std = []
        image_avg_l = np.mean(image[:, :, 0])
        image_std_l = np.std(image[:, :, 0])
        image_avg_a = np.mean(image[:, :, 1])
        image_std_a = np.std(image[:, :, 1])
        image_avg_b = np.mean(image[:, :, 2])
        image_std_b = np.std(image[:, :, 2])
        avg.append(image_avg_l)
        avg.append(image_avg_a)
        avg.append(image_avg_b)
        std.append(image_std_l)
        std.append(image_std_a)
        std.append(image_std_b)
        return (avg, std)

    def fit(self,images, save_dir="./", methods="Reinhard", color_space="LAB", random_shuffle=False, n=0):

        labL_avg_List = []
        labA_avg_List = []
        labB_avg_List = []
        labL_std_List = []
        labA_std_List = []
        labB_std_List = []

        images, image_names = LoadImages(images)
        if random_shuffle:
            random.shuffle(images)
            
        for img in images:
            try:
                if color_space == "LAB":
                    img = cv2.cvtColor(img, cv2.COLOR_BGR2LAB)
                elif color_space == "HED":
                    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
                    img = color.rgb2hed(img)
                elif color_space == "HSV":
                    img = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
                img_avg, img_std = self._getavgstd(img)
            except Exception as e:
                print(f"Error processing image")
                continue

            labL_avg_List.append(img_avg[0])
            labA_avg_List.append(img_avg[1])
            labB_avg_List.append(img_avg[2])
            labL_std_List.append(img_std[0])
            labA_std_List.append(img_std[1])
            labB_std_List.append(img_std[2])

        l_avg_mean = np.mean(labL_avg_List).item()
        l_avg_std = np.std(labL_avg_List).item()
        l_std_mean = np.mean(labL_std_List).item()
        l_std_std = np.std(labL_std_List).item()
        a_avg_mean = np.mean(labA_avg_List).item()
        a_avg_std = np.std(labA_avg_List).item()
        a_std_mean = np.mean(labA_std_List).item()
        a_std_std = np.std(labA_std_List).item()
        b_avg_mean = np.mean(labB_avg_List).item()
        b_avg_std = np.std(labB_avg_List).item()
        b_std_mean = np.mean(labB_std_List).item()
        b_std_std = np.std(labB_std_List).item()
        
        std_avg_list = [
        labL_avg_List,
        labL_std_List,
        labA_avg_List,
        labA_std_List,
        labB_avg_List,
        labB_std_List,
        ]
        
        distribution = []
        for std_avg in std_avg_list:
            f = Fitter(std_avg, distributions=["norm", "laplace"])
            f.fit()
            distribution.append(list(f.get_best(method="sumsquare_error").keys())[0])

        yaml_dict_lab = {
            "random": random_shuffle,
            "n_each_class": n,
            "color_space": color_space,
            "methods": methods,
            "{}".format(color_space[0]): {  # lab-L/hed-H
                "avg": {
                    "mean": round(l_avg_mean, 3),
                    "std": round(l_avg_std, 3),
                    "distribution": distribution[0],
                },
                "std": {
                    "mean": round(l_std_mean, 3),
                    "std": round(l_std_std, 3),
                    "distribution": distribution[1],
                },
            },
            "{}".format(color_space[1]): {  # lab-A/hed-E
                "avg": {
                    "mean": round(a_avg_mean, 3),
                    "std": round(a_avg_std, 3),
                    "distribution": distribution[2],
                },
                "std": {
                    "mean": round(a_std_mean, 3),
                    "std": round(a_std_std, 3),
                    "distribution": distribution[3],
                },
            },
            "{}".format(color_space[2]): {  # lab-B/hed-D
                "avg": {
                    "mean": round(b_avg_mean, 3),
                    "std": round(b_avg_std, 3),
                    "distribution": distribution[4],
                },
                "std": {
                    "mean": round(b_std_mean, 3),
                    "std": round(b_std_std, 3),
                    "distribution": distribution[5],
                },
            },
        }
        
        yaml_save_path = "{dataset_name}-config.yaml"
        with open(yaml_save_path, "w") as f:
            yaml.dump(yaml_dict_lab, f)
            print("The dataset lab statistics has been saved in {}".format(yaml_save_path))

    def transfrom(images,yaml_file: Optional[str] = "{dataset_name}-config.yaml",
        save_dir_path: Optional[str] = './randstainna_result/',
        std_hyper: Optional[float] = 0,
        distribution: Optional[str] = "normal",
        probability: Optional[float] = 1.0,
        is_train: Optional[bool] = True
        ):

        randstainna = RandStainNAAdaptor(
            yaml_file = yaml_file,
            std_hyper = std_hyper,
            distribution = distribution,
            probability = probability,
            is_train = is_train
        )

        images, image_names = LoadImages(images)
        
        if not os.path.exists(save_dir_path):
            os.mkdir(save_dir_path)

        for i,img in enumerate(images):
            img = randstainna(img)
            SaveImages([img],save_dir_path,image_names[image_names[i]])

    
# TODO test it 