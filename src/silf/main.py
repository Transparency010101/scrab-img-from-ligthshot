"""This file is center of whole programm

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
    >>> python3 src/main -h
    >>> poetry run silf -h
    >>> silf -h

Functions:
    main: Enter point in program
"""

import time
import os

from .cli import cli
from .scrab_img_from_lightshot import ScrabImgFromLightShot as silf
from .ect import (
    create_img_folder_if_not_exist,
    do_delete_all_images,
)


def main():
    """Enter point in program"""
    start_program_time = time.time()

    cli_args = cli()
    create_img_folder_if_not_exist()
    do_delete_all_images(cli_args.delete_images)
    silf.start_downloading_images(cli_args.count_of_images)

    print(f"All time: {int(time.time() - start_program_time)}")
