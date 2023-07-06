"""Download images from Lightshot's site

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

Usage:
    python ./src/main.py or python3 ./src/main.py

Functions:
    do_delete_all_images
    main
"""

import time
import os

from core import ScrabImgFromLightShot


def do_delete_all_images():
    """Delete all images from folder img/

    It did it for convince, to don't delete it manually. There are 2 choices to
    delete it, or not, for convince.

    Returns:
        None
    """
    if len(os.listdir("img/")) != 0:
        permission_for_delete_images = input(
            "Do you want delete all images from folder, (y - yes, n - no) "
        )
        if permission_for_delete_images == "y":
            for folder, _, files in os.walk("img/"):
                for file in files:
                    os.remove(folder + file)
        elif permission_for_delete_images == "n":
            pass
        else:
            print("Incorrect input, try again")


def main(number_of_images, debug_mod=False):
    """Enter point in program.

    Arguments:
        number_of_images (int): number of images, that need to download
        debug_mod (bool): turn on/off debug mod

    Returns:
        None
    """
    do_delete_all_images()

    start_program_time = time.time()
    # Need to rewrite this comment, it doesn't give enough truly information
    # When this code(in while loop) executing, sometimes errors occur due to
    # the lack of a link, or it could not be obtained, and so that the program
    # does not stop - an endless loop wrapped in try/except, which absorbs all
    # errors, and ignores them. But there's a nuance - bugs(that I accidentally
    # made while developing) are not shown due to try/catch, so there is
    # debug_mod in function 'main'
    while number_of_images != len(os.listdir("img/")):
        try:
            ScrabImgFromLightShot.download_img()
        except Exception as error:
            if debug_mod:
                print("SOMETHING WENT WRONG!:")
                print(error)
            pass

    print(f"All time: {int(time.time() - start_program_time)}")


if __name__ == "__main__":
    number_of_images = int(input("How many images to download(default=10): ")
                           or 10)
    # May occur, that folder img/ doesn't exist, and will be an error.
    try:
        main(int(number_of_images))
    except FileNotFoundError:
        # If you work in pycharm or another code editor/IDE, check the
        # "working directory"(in Configuration, where Running the scripts)
        # there must be root name of this project, not folder src or else.
        # Folder img must be in root directory.
        os.mkdir("img")
        main(int(number_of_images))

