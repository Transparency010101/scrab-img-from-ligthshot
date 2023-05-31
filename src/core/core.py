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

import string
import random
import requests

from bs4 import BeautifulSoup
from fake_useragent import UserAgent


class ScrabImgFromLightShot:
    header = {
        "User-Agent": None,
        "Accept": "*/*"
    }

    @staticmethod
    def create_random_six_symbols():
        lower_case = string.ascii_lowercase
        numbers = string.digits
        use_for = lower_case + numbers
        length = 6

        return "".join(random.sample(use_for, length))

    @staticmethod
    def create_random_name_for_img():
        lower_case = string.ascii_lowercase
        upper_case = string.ascii_uppercase
        numbers = string.digits
        length = 8

        use_for = lower_case + upper_case + numbers

        return "".join(random.sample(use_for, length))

    @staticmethod
    def is_img_broken(img):
        """
        Sometimes get broken images, they have not size more 1000 bytes.
        """
        min_amount_of_bytes = 1000
        return len(img.content) > min_amount_of_bytes

    @classmethod
    def get_url_of_img(cls):
        """
        Get a link on a html page. Parse <img/> with the id of the 'screenshot-image',
        and get the url to img and then return it.
        """
        cls.header["User-Agent"] = UserAgent().random

        html_code = requests.get(
            f"https://prnt.sc/image/{cls.create_random_six_symbols()}",
            headers=cls.header
        ).text

        url_of_img = BeautifulSoup(html_code, "lxml").find("img", {
            "id": "screenshot-image"
        }).get("src")

        return url_of_img

    @classmethod
    def download_img(cls):
        request_url_of_img = requests.get(cls.get_url_of_img(), headers=cls.header)
        if cls.is_img_broken(request_url_of_img):
            img_name = f"img/test_{cls.create_random_name_for_img()}" + ".jpg"

            with open(img_name, "wb") as img:
                img.write(request_url_of_img.content)
