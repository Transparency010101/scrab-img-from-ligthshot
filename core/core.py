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
        length = 10

        use_for = lower_case + upper_case + numbers

        return "".join(random.sample(use_for, length))

    def get_url_of_img(self):
        self.header["User-Agent"] = UserAgent().random

        html_code_with_img = requests.get(
            f"https://prnt.sc/image/{self.create_random_six_symbols()}",
            headers=self.header
        ).text

        url_of_img = BeautifulSoup(html_code_with_img, "lxml").find("img", {
            "id": "screenshot-image"
        }).get("src")

        return url_of_img

    def download_img(self):
        request_url_of_img = requests.get(self.get_url_of_img(), headers=self.header)
        min_amount_of_bytes = 1000
        if len(request_url_of_img.content) > min_amount_of_bytes:
            img_name = f"img/test_{self.create_random_name_for_img()}" + ".jpg"

            with open(img_name, "wb") as img_opt:
                img_opt.write(request_url_of_img.content)