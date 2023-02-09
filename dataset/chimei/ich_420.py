import os

from ..dataset import Dataset


class ICH420(Dataset):
    def __init__(self):
        super().__init__(os.environ["DATASET_ICH_420"])
        self.__segmentation_dir = os.path.join(self.folder_path, "ImageSets", "Segmentation")
        self.__image_dir = os.path.join(self.folder_path, "Images")
        self.__label_dir = os.path.join(self.folder_path, "Labels")

    @property
    def train_image_filepaths(self) -> [str]:
        return self.__load_from_imageset(self.__image_dir, "train.txt")

    @property
    def train_label_filepaths(self) -> [str]:
        return self.__load_from_imageset(self.__label_dir, "train.txt")

    @property
    def test_image_filepaths(self) -> [str]:
        return self.__load_from_imageset(self.__image_dir, "val.txt")

    @property
    def test_label_filepaths(self) -> [str]:
        return self.__load_from_imageset(self.__label_dir, "val.txt")

    def __load_from_imageset(self, image_dir, image_set_type):
        with open(os.path.join(self.__segmentation_dir, image_set_type),
                  "r", encoding="utf-8") as seg_file:
            return [os.path.join(image_dir, filename)
                    for filename in seg_file.read().split("\n")[1:-1]]