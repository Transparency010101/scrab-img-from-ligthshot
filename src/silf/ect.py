"""This module contain necessary functions for good working, or convince

License:
    Copyright 2023 Transparency010101

    Licensed under the Apache License, Version 2.0 (the "License");
    you may not use this file except in compliance with the License.
    You may obtain a copy of the License at

        http://www.apache.org/licenses/LICENSE-2.0

    Unless required by applicable law or agreed to in writing, software
    distributed under the License is distributed on an "AS IS" BASIS,
    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
    See the License for the specific language governing permissions and
    limitations under the License.

Foreword:
    I'm trying to observe standards of code writing on Python(PEP8)

Functions:
    create_img_folder_if_not_exist: Create folder img/ if it doesn't exist.
    delete_all_images: Delete all images from folder img/
"""

import os

from .scrab_img_from_lightshot import (
    ScrabImgFromLightShot,
    PATH_TO_FOLDER_IMG
)


def create_img_folder_if_not_exist():
    """Create folder img/ if it doesn't exist.

    If folder img/ doesn't exist will be an error, so need to check this every
    time when program starts.

    Returns:
        None
    """
    if not os.path.exists(PATH_TO_FOLDER_IMG):
        os.makedirs(os.path.dirname(PATH_TO_FOLDER_IMG))


def do_delete_all_images(to_delete):
    """Delete all images from folder img/

    It did it for convince, to don't delete it manually. There are 2 choices to
    delete it, or not, for convince. And it's option, if folder img/ contain
    some images.

    Arguments:
        to_delete (bool): to delete images from folder img/

    Returns:
        None
    """
    if len(os.listdir(PATH_TO_FOLDER_IMG)) != 0:
        if to_delete:
            for folder, _, files in os.walk(PATH_TO_FOLDER_IMG):
                for file in files:
                    os.remove(folder + file)
        elif not to_delete:
            pass
        else:
            print("Incorrect input, try again")
