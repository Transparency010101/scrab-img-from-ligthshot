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

Usage:
    python ./src/main.py or python3 ./src/main.py

Functions:
    create_img_folder_if_not_exist
    delete_all_images
    somethings_went_wrong
    main
"""

import time
import os

from core import ScrabImgFromLightShot

# Check file img/temp
def create_img_folder_if_not_exist():
    """Create folder img/ if it doesn't exist.

    If folder img/ doesn't exist will be an error, so need to check this every
    time when program starts.

    Returns:
        None
    """
    if not os.path.exists("img/"):
        os.makedirs(os.path.dirname("img/"))


def delete_all_images():
    """Delete all images from folder img/

    It did for convince, to don't delete it manually. And this function call
    every time when program starts.

    Returns:
        None
    """
    # Need to do accepting, "Do you want to delete all uploaded images?"
    # If yes - delete, if no - quo it
    for folder, _, files in os.walk("img/"):
        for file in files:
            os.remove(folder + file)


def main(number_of_images, debug_mod=False):
    """Enter point in program.

    Arguments:
        number_of_images (int):
        debug_mod (bool):

    Returns:
        None
    """
    create_img_folder_if_not_exist()
    delete_all_images()

    start_program_time = time.time()
    # When this code(in while loop) executing, sometimes errors occur due to
    # the lack of a link, or it could not be obtained, and so that the program
    # does not stop - an endless loop wrapped in try/except, which absorbs all
    # errors, and ignores them. But there's a nuance - bugs(that I accidentally
    # made while developing) are not shown due to try/catch, so there is
    # debug_mod in function 'main'
    while number_of_images != len(os.listdir("img/")):
        try:
            ScrabImgFromLightShot.download_img()
        except Exception as err:
            if debug_mod:
                print("SOMETHING WENT WRONG!")
                print(err)
            pass
    print(f"All time: {int(time.time() - start_program_time)}")


if __name__ == "__main__":
    main(int(input("How many images to download(default=10): ") or 10))
