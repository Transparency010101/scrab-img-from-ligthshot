"""This module provide only CLI interface

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
    delete_all_images_from_folder()
"""
import unittest
import os

import src.silf.cli as cli
import src.silf.ect as ect
import src.silf.scrab_img_from_lightshot as silf


def delete_all_images_from_folder():
    """Delete images from folder img/

    Returns:
        None
    """
    for folder, _, files in os.walk("img/"):
        for file in files:
            os.remove(folder + file)


class ScrabImgFromLightshot(unittest.TestCase):
    def test_download_1_image(self):
        delete_all_images_from_folder()
        silf.ScrabImgFromLightShot.download_img()
        self.assertEqual(len(os.listdir("img/")), 1)
        delete_all_images_from_folder()
