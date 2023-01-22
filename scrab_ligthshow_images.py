import requests

from random import sample
from bs4 import BeautifulSoup


def create_random_six_symbols():
    lower_case = "abcdefghijklmnopqrstuvwxyz"
    numbers = "1234567890"
    use_for = lower_case + numbers
    length_for_pass = 6
    result = "".join(sample(use_for, length_for_pass))

    return result


header = {
    "User-Agent": "Mozilla/5.0 (Android 10; Mobile; rv:91.0) Gecko/91.0 Firefox/91.0",
    "Accept": "*/*"
}

site_with_img = requests.get(f"https://prnt.sc/image/{create_random_six_symbols()}", headers=header).text

img_url = BeautifulSoup(site_with_img, "lxml").find("img", {"id":"screenshot-image"}).get("src")
img_request = requests.get(img_url, headers=header)
img_opt = open("img/test1" + ".jpg", "wb")
img_opt.write(img_request.content)
