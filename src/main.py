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
    python src/main.py <number> [, -y, -n]
    <number> - number of images
    [, -y, -n] - Option arguments. Do you want to delete all images from folder
        -y - yes, -n - no

Functions:
    create_img_folder_if_not_exist()
    delete_all_images
    main
"""

import time
import os
import sys

from download_images import ScrabImgFromLightShot


def create_img_folder_if_not_exist():
    """Create folder img/ if it doesn't exist.

    If folder img/ doesn't exist will be an error, so need to check this every
    time when program starts.

    Returns:
        None
    """
    if not os.path.exists("img/"):
        os.makedirs(os.path.dirname("img/"))


def delete_all_images(choise="-y"):
    """Delete all images from folder img/

    It did it for convince, to don't delete it manually. There are 2 choices to
    delete it, or not, for convince.

    Returns:
        None
    """
    if len(os.listdir("img/")) != 0:
        if choise == "-y":
            for folder, _, files in os.walk("img/"):
                for file in files:
                    os.remove(folder + file)
        elif choise == "-n":
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

    # When this code(in while loop) executing, sometimes errors occur due to
    # the lack of a link, or it could not be obtained, and so that the program
    # does not stop - an endless loop wrapped in try/except, which absorbs all
    # errors, and ignores them. But there's a nuance - bugs(that I accidentally
    # made while developing) are not shown due to try/catch, so there is
    # debug_mod in function 'main'.
    while number_of_images != len(os.listdir("img/")):
        try:
            ScrabImgFromLightShot.download_img()
        except Exception as error:
            if debug_mod:
                print("SOMETHING WENT WRONG!:")
                print(error)
            pass


if __name__ == "__main__":
    start_program_time = time.time()

    create_img_folder_if_not_exist()

    arguments_of_command_line = sys.argv
    try:
        # This is optional argument -y or -n
        # I don't know to do it right, so if you clearly didn't indicate
        # it(in console) will be an IndexError, and then func will work with
        # argument by default(-y).
        delete_all_images(arguments_of_command_line[2])
        main(int(int(arguments_of_command_line[1])))
    except IndexError:
        delete_all_images()
    finally:
        main(int(int(arguments_of_command_line[1])))

    print(f"All time: {int(time.time() - start_program_time)}")
