import os
from typing import Optional, List

from .ich import ICHType
from .img import ImageType

class ICHImage(object):
    def __init__(self, image_filepath: os.path, mask_images: Optional[List[os.path]] = None):
        self.__image_filepath: os.path = image_filepath,
        self.__mask_images: Optional[List[os.path]]= mask_images
        self.__image_type: Optional[ImageType] = None
        self.__ich_types: Optional[ICHType] = None
