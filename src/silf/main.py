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
    main()
"""

import time
import os

from .cli import cli
from .ect import (
    create_img_folder_if_not_exist,
    do_delete_all_images,
    start_downloading
)


def main():
    """Enter point in program"""
    start_program_time = time.time()

    cli_args = cli()
    create_img_folder_if_not_exist()
    do_delete_all_images(cli_args.delete_images)
    start_downloading(cli_args.count_of_images)

    print(f"All time: {int(time.time() - start_program_time)}")
