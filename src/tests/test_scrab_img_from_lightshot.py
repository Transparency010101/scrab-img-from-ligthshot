"""Tests for functionally in scrab_img_from_lightshot.py

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

classes:
    ScrabImgFromLightshot: testing the class ScrabImgFromLightshot
"""

import unittest
import os

import src.silf.scrab_img_from_lightshot as silf

from tests.test import delete_all_images_from_folder
from src.silf.scrab_img_from_lightshot import PATH_TO_FOLDER_IMG


class ScrabImgFromLightshot(unittest.TestCase):
    def test_work_correctly(self):
        delete_all_images_from_folder()
        silf.ScrabImgFromLightShot.start_downloading_images(1)
        self.assertEqual(len(os.listdir(PATH_TO_FOLDER_IMG)), 1)
        delete_all_images_from_folder()

    def test_download_certain_number_of_images(self):
        delete_all_images_from_folder()
        silf.ScrabImgFromLightShot.start_downloading_images(3)
        self.assertEqual(len(os.listdir(PATH_TO_FOLDER_IMG)), 3)
        delete_all_images_from_folder()
