import requests

from random import sample, choice
from bs4 import BeautifulSoup

desktop_agents = [
    # Tor Browser for Windows and Linux
    'Mozilla/5.0 (Windows NT 10.0; rv:78.0) Gecko/20100101 Firefox/78.0',
    # Tor Browser for Android
    'Mozilla/5.0 (Android 10; Mobile; rv:91.0) Gecko/91.0 Firefox/91.0',
    'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
    'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_1) '
    'AppleWebKit/602.2.14 (KHTML, like Gecko) Version/10.0.1 Safari/602.2.14',
    'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.71 Safari/537.36',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_1) '
    'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.98 Safari/537.36',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) '
    'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.98 Safari/537.36',
    'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.71 Safari/537.36',
    'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:50.0) Gecko/20100101 Firefox/50.0'
]

number_of_images = input("How many images to download(default 10): ") or 10


class Main:

    header = {
        "User-Agent": None,
        "Accept": "*/*"
    }

    def create_random_six_symbols(self):
        lower_case = "abcdefghijklmnopqrstuvwxyz"
        numbers = "1234567890"
        use_for = lower_case + numbers
        length_for_pass = 6

        return "".join(sample(use_for, length_for_pass))

    def create_random_name_for_img(self):
        lower_case = "abcdefghijklmnopqrstuvwxyz"
        upper_case = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        numbers = "1234567890"
        length_for_pass = 10

        use_for = lower_case + upper_case + numbers

        return "".join(sample(use_for, length_for_pass))

    def get_url_of_img(self):
        self.header["User-Agent"] = choice(desktop_agents)

        site_with_img = requests.get(
            f"https://prnt.sc/image/{self.create_random_six_symbols()}",
            headers=self.header
        ).text

        url_of_img = BeautifulSoup(site_with_img, "lxml").find("img", {
            "id": "screenshot-image"
        }).get("src")

        return url_of_img

    def download_img(self):
        get_img = requests.get(self.get_url_of_img(), headers=self.header)
        img_name = f"../img/test_{self.create_random_name_for_img()}" + ".jpg"

        img_opt = open(img_name, "wb")

        img_opt.write(get_img.content)


if __name__ == "__main__":
    while True:
        try:
            Main().download_img()
        except Exception:
            continue
