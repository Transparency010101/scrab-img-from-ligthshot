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
    See in README file

Functions:
    create_img_folder_if_not_exist()
    delete_all_images
    main
"""

import time
import os
import sys
import argparse

from scrab_img_from_lightshot import ScrabImgFromLightShot


def create_img_folder_if_not_exist():
    """Create folder img/ if it doesn't exist.

    If folder img/ doesn't exist will be an error, so need to check this every
    time when program starts.

    Returns:
        None
    """
    if not os.path.exists("img/"):
        os.makedirs(os.path.dirname("img/"))


def delete_all_images(to_delete):
    """Delete all images from folder img/

    It did it for convince, to don't delete it manually. There are 2 choices to
    delete it, or not, for convince.

    Arguments:
        to_delete (bool): to delete images from folder img/

    Returns:
        None
    """
    if len(os.listdir("img/")) != 0:
        if to_delete:
            for folder, _, files in os.walk("img/"):
                for file in files:
                    os.remove(folder + file)
        elif not to_delete:
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

    cli_parser = argparse.ArgumentParser(
        prog="silf",
        description="This program download images from ligthshot's site"
    )
    cli_parser.add_argument(
        "count_of_images",
        help="Just print hello world",
        type=int
    )
    cli_parser.add_argument(
        "-D", "--delete_images",
        action="store_false",
        help="to don't delete images in folder",
        default=True
    )
    cli_args = cli_parser.parse_args()

    create_img_folder_if_not_exist()
    delete_all_images(cli_args.delete_images)
    main(cli_args.count_of_images)

    print(f"All time: {int(time.time() - start_program_time)}")
