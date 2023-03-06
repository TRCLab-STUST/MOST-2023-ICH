from typing import Optional, List

from . import ICHType
from ..file import ImageType


class ICHImage(object):
    def __init__(self, image_filepath: str, mask_images: Optional[List[str]] = None):
        self.__image_filepath: str = image_filepath
        self.__mask_images: Optional[List[str]] = mask_images
        self.__image_type: Optional[ImageType] = None
        self.__ich_types: ICHType = ICHType.NOT_ANY

    @property
    def ich_types(self):
        return self.__ich_types

    @ich_types.setter
    def ich_types(self, new_ich_types):
        self.__ich_types = new_ich_types
