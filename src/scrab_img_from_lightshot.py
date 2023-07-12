"""This module provide class which purpose is downloading images from Lightshot

Licence:
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
    I trying to observe standard code writing on python(PEP8)

Classes:
    ScrabImgFromLightShot
"""

import string
import random
import requests

from bs4 import BeautifulSoup
from fake_useragent import UserAgent


class ScrabImgFromLightShot:
    """Downloading images from Lightshot
    
    Attributes:
        header (dict): for browser to think that I'm not a robot
    """

    header = {
        "User-Agent": None,
        "Accept": "*/*"
    }

    @staticmethod
    def create_random_six_symbols():
        """Create string that consist 6 random symbols for link
        
        The thing is need to pick up a link for image, and to do it need 6
        random english letters in upper and lower case and numbers from 0 to 9.
        See on top of README file, there is example(in paragraph 'What Is It?')

        Returns:
            string
        """
        lower_case = string.ascii_lowercase
        numbers = string.digits
        use_for = lower_case + numbers
        length = 6

        return "".join(random.sample(use_for, length))

    @staticmethod
    def create_random_name_for_img():
        """Create random name for downloaded image
        
        Returns:
            string
        """
        lower_case = string.ascii_lowercase
        upper_case = string.ascii_uppercase
        numbers = string.digits
        length = 8

        use_for = lower_case + upper_case + numbers

        return "".join(random.sample(use_for, length))

    @staticmethod
    def is_img_broken(img):
        """Check is image broken

        Broken images have not size more 1000 bytes.

        Arguments:
            img (bytes): it's literally image in bytes

        Return:
            bool
        """
        min_amount_of_bytes = 1000
        return len(img) < min_amount_of_bytes

    @classmethod
    def get_url_of_img(cls):
        """Get image's url
        
        Get a link on a html page. Parse html tag <img/> with the id of the
        'screenshot-image', and get the url to img and then return it.
        
        Returns:
            string
        """
        cls.header["User-Agent"] = UserAgent().random

        page = requests.get(
            f"https://prnt.sc/image/{cls.create_random_six_symbols()}",
            headers=cls.header
        ).text

        url_of_img = BeautifulSoup(page, "lxml").find("img", {
            "id": "screenshot-image"
        }).get("src")

        return url_of_img

    @classmethod
    def download_img(cls):
        """Download images and put them in folder img/"""
        request_url_of_img = requests.get(cls.get_url_of_img(),
                                          headers=cls.header)
        # Is image broken - True, then I shouldn't admit it.
        # Is image broken - False, so I should to admit it,
        # but "if" statement will not execute, because value isn't True,
        # so it toggled from False to True by operator "not"
        if not (cls.is_img_broken(request_url_of_img.content)):
            img_name = f"img/img_{cls.create_random_name_for_img()}" + ".jpg"

            with open(img_name, "wb") as img:
                img.write(request_url_of_img.content)
