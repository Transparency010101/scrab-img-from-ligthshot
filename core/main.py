import requests
import time

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


class Main:
    header = {
        "User-Agent": None,
        "Accept": "*/*"
    }

    @staticmethod
    def create_random_six_symbols():
        lower_case = "abcdefghijklmnopqrstuvwxyz"
        numbers = "1234567890"
        use_for = lower_case + numbers
        length_for_pass = 6

        return "".join(sample(use_for, length_for_pass))

    @staticmethod
    def create_random_name_for_img():
        lower_case = "abcdefghijklmnopqrstuvwxyz"
        upper_case = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        numbers = "1234567890"
        length_for_pass = 10

        use_for = lower_case + upper_case + numbers

        return "".join(sample(use_for, length_for_pass))

    def get_url_of_img(self):
        self.header["User-Agent"] = choice(desktop_agents)

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
            img_name = f"../img/test_{self.create_random_name_for_img()}" + ".jpg"

            with open(img_name, "wb+") as img_opt:
                img_opt.write(request_url_of_img.content)


if __name__ == "__main__":
    number_of_images = int(input("How many images to download(default 1): ")) or 1

    start_program_time = time.time()
    for _ in range(number_of_images):
        start_cycle = time.time()
        try:
            Main().download_img()
        except Exception:
            continue
        finally:
            print(f">>> {time.time() - start_cycle}")
    print(f"All time: {time.time() - start_program_time}")
