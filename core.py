import requests

from random import choice
from time import sleep
from bs4 import BeautifulSoup

from other import *

number_of_images = input("How many images to download(default 10): ") or 10


def main():
    header = {
        "User-Agent": None,
        "Accept": "*/*"
    }

    seconds = 2
    sleep(seconds)

    header["User-Agent"] = choice(desktop_agents)

    site_with_img = requests.get(
        f"https://prnt.sc/image/{create_random_six_symbols()}",
        headers=header
    ).text

    img_url = BeautifulSoup(site_with_img, "lxml").find("img", {
        "id": "screenshot-image"
    }).get("src")

    img_request = requests.get(img_url, headers=header)
    img_opt = open(
        f"img/test_{create_random_name_for_img()}" + ".jpg", "wb"
    )
    img_opt.write(img_request.content)


if __name__ == "__main__":
    while True:
        try:
            main()
        except Exception:
            continue
