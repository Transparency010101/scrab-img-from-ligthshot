![PyPI - Python Version](https://img.shields.io/pypi/pyversions/poetry)
![Static Badge](https://img.shields.io/badge/poetry-1.4%2B-green)
![Static Badge](https://img.shields.io/badge/only_linux_support-green)
![Static Badge](https://img.shields.io/badge/pass_tests-none-red)
![GitHub issues](https://img.shields.io/github/issues-raw/Transparency010101/scrab-img-from-ligthshot)


# Scrab Img(images) From LightShot

## What Is It?
If you open this link https://prnt.sc/image/4fdgjb, you can see an image of someone user of lightshot.
You can change lasts 6 symbols in the link, and you'll see another image: https://prnt.sc/image/afsghb,
but changing it manually is uncomfortable. To automatic this uncomfortable process, I created this project.

Script will download certain count(that you indicate) of images
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

### With Pip
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

Then launch this command in the ***root***(scrab-img-from-lightshot/) project's folder:
```
pip install -r requirements.txt
```
That command will install needed libraries.


## Usage
See more in help: `python3 src/main.py -h`

### Launch program:

Python:
```
python3 src/main.py 10 
```

```
python3 src/main.py 3 -D
```

Poetry:
```
poetry run python3 src/main.py 7 
```
or
```
poetry run python3 src/main.py 2 -D
```
When program finished, open the project's folder `scrab-img-from-lightshot/img/`, and there will be images.

## Notes
Idea for the project I got [there](https://www.youtube.com/watch?v=OUki27mlwOw) 4:30.

I'm developing this project only for my practise, maybe there is fools ideas,
controversial points regarding the development, not serious thing, attitude towards whole development

P.S. Не бейте за англиский.


