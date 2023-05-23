import ect
import time
import os

from core import ScrabImgFromLightShot


def main(count_items: int, debug_mod=False):
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
                print("<!============================================!>")
                print("SOMETHING WENT WRONG!")
                print("<!============================================!>")
                print(err)
            pass
    print(f"All time: {int(time.time() - start_program_time)}")


if __name__ == "__main__":
    ect.delete_images()
    ect.create_img_folder_if_not_exist()

    count_of_images = input("How many images to download(default=10): ") or 10

    main(int(count_of_images))
