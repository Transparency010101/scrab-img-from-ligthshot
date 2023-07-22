"""Tests for functionally in ect.py

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

Classes:
    DoDeleteAllImages: test for function do_delete_all_images
"""

import os
import unittest

import src.silf.scrab_img_from_lightshot as silf
import src.silf.ect as ect

from src.silf.scrab_img_from_lightshot import PATH_TO_FOLDER_IMG


class DoDeleteAllImages(unittest.TestCase):
    def test_delete_images(self):
        silf.ScrabImgFromLightShot.start_downloading_images(2)
        ect.do_delete_all_images(True)
        self.assertEqual(len(os.listdir(PATH_TO_FOLDER_IMG)), 0)

    def test_do_not_delete_images(self):
        silf.ScrabImgFromLightShot.start_downloading_images(2)
        ect.do_delete_all_images(False)
        self.assertEqual(len(os.listdir(PATH_TO_FOLDER_IMG)), 2)
