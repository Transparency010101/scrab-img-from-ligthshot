# Copyright 2023 Transparency010101
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.


import time
import os

from core import etc
from core import ScrabImgFromLightShot


def main(count_items: int, debug_mod=False):
    """
    When executing the code, sometimes errors occur due to the lack of a link, or it
    could not be obtained, and so that the program does not stop - an endless loop
    wrapped in try/catch, which absorbs all exceptions, and ignores them.
    But there is a nuance that errors are not shown due to try/catch, so there is
    debug_mod in function 'main'
    """
    start_program_time = time.time()
    while count_items != len(os.listdir("img/")):
        try:
            ScrabImgFromLightShot.download_img()
        except Exception as err:
            if debug_mod:
                etc.somethings_went_wrong()
                print(err)
            pass
    print(f"All time: {int(time.time() - start_program_time)}")


if __name__ == "__main__":
    etc.create_img_folder_if_not_exist()
    etc.delete_images()

    count_of_images = input("How many images to download(default=10): ") or 10

    main(int(count_of_images))
