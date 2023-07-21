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