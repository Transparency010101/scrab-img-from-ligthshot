# Scrab Img From LightShot

# What is it
if you open this link https://prnt.sc/image/4fdgjb, you can see an images of someone user.
You can some change lasts symbols, and you'll see another image(https://prnt.sc/image/afsghb), but not always.
To automatic this process I created this project on python.

# How to use
Firstly, you have to install python3. Create virtual venv in this project, open terminal in project's
folder and launch venv: <br>
**Linux**: `source venv/bin/activate` <br>
**Windows** `venv/Scripts/activate` <br>
Then launch this command in terminal: `pip install -r requirements.txt`
After installation launch this command: `python core/main.py` or `python3 core/main.py`

First input - it's approximately count of images, which would to download, why approximately? Well my program work so. <br>
Second input - it's by one time you can download several images. <br/>
Example:
    2 -> two images will download by one time,
    3 -> three images will download by one time

But I recommended to input max 2(you can be banned by site)
When program finished, open in the project folder img, and there will be images.

P.S Не бейте за англишь и/или русский, мне похуй.

# Addiction
In config.py(in folder core) you can change default settings