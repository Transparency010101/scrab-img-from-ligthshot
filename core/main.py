import time
import os

from core import ScrabImgFromLightShot


def create_img_folder_if_not_exist():
    """Если не будет существовать папка img/ будет выдавать ошибку"""
    if not os.path.exists("img/"):
        os.makedirs(os.path.dirname("img/"))


def delete_images():
    for folder, _, files in os.walk("img/"):
        for file in files:
            os.remove(folder + file)


def loop(items: int, debug_mod: bool = True):
    """
    При выполнение кода иногда возникают ошибки связаые с отсутствием ссылки,
    и что бы программа не останавливалась оно обернуто в try catch
    """
    start_program_time = time.time()
    while items != len(os.listdir("img/")):
        try:
            ScrabImgFromLightShot().download_img()
        except Exception as err:
            if debug_mod:
                print(err)
            pass
    print(f"All time: {int(time.time() - start_program_time)}")


if __name__ == "__main__":
    delete_images()

    count_of_images = int(input("How many images to download(default=5): ")) or 5

    create_img_folder_if_not_exist()
    loop(count_of_images)
