import os
import asyncio
import httpx as htx

from random import sample, choice
from bs4 import BeautifulSoup
from time import time

from config import (
    debug_mod,
    default_count_of_image
)

desktop_agents = [
    'Mozilla/5.0 (Windows NT 10.0; rv:78.0) Gecko/20100101 Firefox/78.0',
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


def create_random_url_path():
    lower_case = "abcdefghijklmnopqrstuvwxyz"
    numbers = "1234567890"
    use_for = lower_case + numbers
    length_for_pass = 6

    return "".join(sample(use_for, length_for_pass))


def create_random_name_for_img():
    lower_case = "abcdefghijklmnopqrstuvwxyz"
    upper_case = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    numbers = "1234567890"
    length_for_pass = 10

    use_for = lower_case + upper_case + numbers

    return "".join(sample(use_for, length_for_pass))


def fake_user_agent():
    header = {
        "User-Agent": choice(desktop_agents),
        "Accept": "*/*"
    }

    return header


async def get_url_of_img(params):
    async with htx.AsyncClient() as response:
        html_code_with_img = await response.get(
            f"https://prnt.sc/image/{create_random_url_path()}",
            params=params
        )

        if html_code_with_img.status_code == 200:
            url_of_img = BeautifulSoup(html_code_with_img, "lxml").find("img", {
                "id": "screenshot-image"
            }).get("src")

            return url_of_img


async def download_img(url_of_img, params):
    async with htx.AsyncClient() as response:
        request_url_of_img = await response.get(url_of_img, params=params)

        min_amount_of_bytes = 1000
        if len(request_url_of_img.content) > min_amount_of_bytes:
            img_name = f"img/test_{create_random_name_for_img()}" + ".jpg"

            with open(img_name, "wb") as img_opt:
                img_opt.write(request_url_of_img.content)


def create_img_folder_if_not_exist():
    if not os.path.exists("img/"):
        os.makedirs(
            os.path.dirname("img/")
        )
    pass


async def download_one_img():
    await download_img(
        await get_url_of_img(fake_user_agent()),
        fake_user_agent()
    )


async def loop():
    queue = asyncio.Queue()
    task_list = []

    for _ in range(int(count_of_images)):
        try:
            for i in range(int(count_of_images)):
                task = asyncio.create_task(download_one_img())
                task_list.append(task)
        except Exception as err:
            if debug_mod:
                print(err)
            pass

    await queue.join()
    await asyncio.gather(*task_list, return_exceptions=debug_mod)


if __name__ == "__main__":
    count_of_images = input("How many images to download: ") or int(default_count_of_image)

    create_img_folder_if_not_exist()

    start_program_time = time()
    asyncio.run(loop())
    print(f"All time: {int(time() - start_program_time)}")
