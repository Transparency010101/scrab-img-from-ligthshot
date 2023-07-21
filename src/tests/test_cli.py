import os
import unittest
import subprocess

import src.silf.cli as cli
import src.silf.scrab_img_from_lightshot as silf

from src.silf.scrab_img_from_lightshot import PATH_TO_FOLDER_IMG
from tests.test import delete_all_images_from_folder


class CLI(unittest.TestCase):
    def test_does_cli_work(self):
        delete_all_images_from_folder()
        input_data = ["2", "-D"]
        subprocess.run(["python3", "src/run.py", input_data[0]])
        self.assertEqual(len(os.listdir(PATH_TO_FOLDER_IMG)), 2)
        delete_all_images_from_folder()

    def test_does_work_with_flag_D(self):
        silf.ScrabImgFromLightShot.start_downloading_images(2)
        input_data = ["4", "-D"]
        subprocess.run(["python3", "src/run.py", input_data[0], input_data[1]])
        self.assertEqual(len(os.listdir(PATH_TO_FOLDER_IMG)), 4)
        delete_all_images_from_folder()
