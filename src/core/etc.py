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

import os


def create_img_folder_if_not_exist():
    """
    If folder img/ wasn't exist, will be an error.
    """
    if not os.path.exists("img/"):
        os.makedirs(os.path.dirname("img/"))


def delete_images():
    for folder, _, files in os.walk("img/"):
        for file in files:
            os.remove(folder + file)


def somethings_went_wrong():
    print("<!============================================!>")
    print("            SOMETHING WENT WRONG!")
    print("<!============================================!>")
