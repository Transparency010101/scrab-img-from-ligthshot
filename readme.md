<div align="center">
    <img src="https://img.shields.io/pypi/pyversions/requests" alt="python-versions">
</div>

# Scrab Img(images) From LightShot

## What Is It?
If you open this link https://prnt.sc/image/4fdgjb, you can see an image of someone user of lightshot.
You can change lasts 6 symbols in the link, and you'll see another image: https://prnt.sc/image/afsghb,
but to changing it is uncomfortable. To automatic this uncomfortable actions, I created this project.

Script will download certain count of images on you machine(PC, notebook)
___

## Installing

### With Poetry
You have to have installed poetry 1.4 or higher.

Install packages:
```
poetry install
```

Activate virtual environment:
```
poetry shell
```

### With Virtual Environment
You have to have installed python 3.7 or higher. 

Create virtual environment: 
```
python -m venv venv 
```
If didn't work:
```
python3 -m venv venv 
```

Then activate(launch) virtual environmen: 
- **Linux**: `source venv/bin/activate`
- **Windows**: `venv/Scripts/activate`

Then launch this command in the ***root***(scrab-img-from-lightshot/) project's folder:
```
pip install -r requirements.txt
```
That command will install needed libraries.


## Usage
To launch program: 
```
python core/main.py
```

You'll see a prompt: input there a count of images which you want to download.
When program finished, open the project's folder `scrab-img-from-lightshot/img/`, and there will be images.

## Notes
Idea for the project I got [there](https://www.youtube.com/watch?v=OUki27mlwOw) 4:30.

P.S. Не бейте за англиский.