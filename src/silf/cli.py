"""This module provide CLI interface

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

Functions:
    cli: CLI interface
"""

import argparse


def cli():
    """CLI interface

    Returns:
        Namespace
    """
    description = """
    This program download images from ligthshot's site. See more in README file
    """
    cli_parser = argparse.ArgumentParser(
            prog="silf",
            description=description)
    cli_parser.add_argument(
            "count_of_images",
            help="Just print hello world",
            type=int)
    cli_parser.add_argument(
            "-D", "--delete_images",
            action="store_false",
            help="to don't delete images in folder",
            default=True)

    return cli_parser.parse_args()
