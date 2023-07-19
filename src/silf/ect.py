import os


def create_img_folder_if_not_exist():
    """Create folder img/ if it doesn't exist.

    If folder img/ doesn't exist will be an error, so need to check this every
    time when program starts.

    Returns:
        None
    """
    if not os.path.exists("img/"):
        os.makedirs(os.path.dirname("img/"))


def delete_all_images(to_delete):
    """Delete all images from folder img/

    It did it for convince, to don't delete it manually. There are 2 choices to
    delete it, or not, for convince.

    Arguments:
        to_delete (bool): to delete images from folder img/

    Returns:
        None
    """
    if len(os.listdir("img/")) != 0:
        if to_delete:
            for folder, _, files in os.walk("img/"):
                for file in files:
                    os.remove(folder + file)
        elif not to_delete:
            pass
        else:
            print("Incorrect input, try again")


def start_downloading(number_of_images, debug_mod=True):
    """Start downloading images

    Arguments:
        number_of_images (int): number of images, that need to download
        debug_mod (bool): turn on/off debug mod

    Returns:
        None
    """
    # While this code executing, sometimes errors occur and that stop program
    # that's why code wrapped in try/except, but there is nuance, bugs that I
    # accidentally made while developing, are not shown, so there is debug mod
    # in function
    while number_of_images != len(os.listdir("img/")):
        try:
            ScrabImgFromLightShot.download_img()
        except Exception as error:
            if debug_mod:
                print("SOMETHING WENT WRONG!:")
                print(error)
            pass
