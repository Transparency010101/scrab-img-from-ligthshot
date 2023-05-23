import os


def create_img_folder_if_not_exist():
    """
    If folder img/ wasn't exist, will be an error.
    """
    if not os.path.exists("img/"):
        os.makedirs(os.path.dirname("img/"))


def delete_images():
    for folder, _, files in os.walk("img/"):
        for file in files:
            os.remove(folder + file)


def somethings_went_wrong():
    print("<!============================================!>")
    print("            SOMETHING WENT WRONG!")
    print("<!============================================!>")
