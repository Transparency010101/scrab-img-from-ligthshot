import time
import os

from core import ScrabImgFromLightShot


def create_img_folder_if_not_exist():
    if not os.path.exists("img/"):
        os.makedirs(os.path.dirname("img/"))


def delete_images():
    for folder, _, files in os.walk("img/"):
        for file in files:
            os.remove(folder + file)


def loop(count_items: int, debug_mod=True):
    """
    When executing the code, sometimes errors occur due to the lack of a link, or it could not be obtained,
    and so that the program does not stop - an endless loop wrapped in try/catch, which absorbs all exceptions,
    and ignores them. But there is a nuance that errors are not shown due to try/catch, so there is debug_mod
    in function 'loop'
    """
    start_program_time = time.time()
    while count_items != len(os.listdir("img/")):
        try:
            ScrabImgFromLightShot.download_img()
        except Exception as err:
            if debug_mod:
                print(err)
            pass
    print(f"All time: {int(time.time() - start_program_time)}")


if __name__ == "__main__":
    delete_images()
    create_img_folder_if_not_exist()

    count_of_images = input("How many images to download(default=5): ") or 5

    loop(int(count_of_images))
