import unittest
import os

import src.silf.scrab_img_from_lightshot as silf

from tests.test import delete_all_images_from_folder
from src.silf.scrab_img_from_lightshot import PATH_TO_FOLDER_IMG


class ScrabImgFromLightshot(unittest.TestCase):
    def test_download_1_image(self):
        # Do you work correctly(can you download 1 image)
        delete_all_images_from_folder()
        silf.ScrabImgFromLightShot.start_downloading_images(1)
        self.assertEqual(len(os.listdir(PATH_TO_FOLDER_IMG)), 1)
        delete_all_images_from_folder()

    def test_download_3_images(self):
        # Do download certain number of images
        delete_all_images_from_folder()
        silf.ScrabImgFromLightShot.start_downloading_images(3)
        self.assertEqual(len(os.listdir(PATH_TO_FOLDER_IMG)), 3)
        delete_all_images_from_folder()
