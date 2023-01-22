import requests
import random

from bs4 import BeautifulSoup


def create_random_six_symbols():
    lower_case = "abcdefghijklmnopqrstuvwxyz"
    numbers = "1234567890"
    use_for = lower_case + numbers
    length_for_pass = 6
    result = "".join(random.sample(use_for, length_for_pass))

    return result


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

header = {
    "User-Agent": None,
    "Accept": "*/*"
}

number_of_images = input("How many images to download(default 3): ") or 3

for i in range(int(number_of_images)):
    header["User-Agent"] = random.choice(desktop_agents)

    site_with_img = requests.get(
        f"https://prnt.sc/image/{create_random_six_symbols()}",
        headers=header
    ).text

    img_url = BeautifulSoup(site_with_img, "lxml").find("img", {"id": "screenshot-image"}).get("src")

    img_request = requests.get(img_url, headers=header)
    img_opt = open(f"img/test_{i}" + ".jpg", "wb")
    img_opt.write(img_request.content)

