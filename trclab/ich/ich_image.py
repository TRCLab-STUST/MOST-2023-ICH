from pathlib import Path
from typing import Optional, List

from . import ICHType
from ..file import ImageType


class ICHImage(object):
    def __init__(self, image_filepath: str, mask_images: Optional[List[str]] = None):
        self.__image_filepath: str = image_filepath
        self.__mask_images: Optional[List[str]] = mask_images
        self.__image_type: Optional[ImageType] = ImageType(Path(self.__image_filepath).suffix[1:])

        # Default setting
        self.__ich_types: ICHType = ICHType.NOT_ANY

    @property
    def image_type(self):
        """
        取的影像類型

        :return: ImageType
        """
        return self.__image_type

    @property
    def ich_types(self):
        """
        取的腦出血類型

        :return: ICHType
        """
        return self.__ich_types

    @ich_types.setter
    def ich_types(self, new_ich_types):
        """
        設置腦出血類型

        :param new_ich_types: ICHType
        """
        self.__ich_types = new_ich_types
