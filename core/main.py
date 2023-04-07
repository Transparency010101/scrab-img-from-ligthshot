import time
import os

from core import ScrabImgFromLightShot


def create_img_folder_if_not_exist():
    """
    Если не будет существовать папка img/ будет выдавать ошибку
    """
    if not os.path.exists("img/"):
        os.makedirs(os.path.dirname("img/"))


def delete_images():
    for folder, _, files in os.walk("img/"):
        for file in files:
            os.remove(folder + file)


def loop(items: int, debug_mod=False):
    """
    При выполнении кода иногда возникают ошибки связаные с отсутствием ссылки, или ее не получилось достать,
    и что бы программа не останавливалась - бесконечный цыкл обернутый в try catch, который вбирает все исключения,
    и их игнорирует. Но есть нюанс, что ошибки не показываются из-за try catch, поэтому есть debug_mod
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

    count_of_images = input("How many images to download(default=5): ") or 5

    create_img_folder_if_not_exist()
    loop(int(count_of_images))
