"""This file run all tests"""

import src.silf.cli as cli
import src.silf.ect as ect
import src.silf.scrab_img_from_lightshot as silf


def delete_all_images_from_folder():
    for folder, _, files in os.walk("img/"):
        for file in files:
            os.remove(folder + file)

