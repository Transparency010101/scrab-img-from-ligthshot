![PyPI - Python Version](https://img.shields.io/pypi/pyversions/poetry)
![PyPI](https://img.shields.io/pypi/v/scrab-img-from-ligthshot)
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

### Poetry
You have to have installed poetry 1.4 or higher.

Spawn virtual environment:
```
poetry shell 
```

Install requirements
```
poetry install
```

### PyPi
You have to have installed python 3.7 or higher. 

Create virtual environment: 
```
python3 -m venv env 
```

Then activate(launch) virtual environment: 
- **Linux**: `source env/bin/activate`

```
pip3 install scrab-img-from-ligthshot
```


### Source
Clone repository:
```
git clone git@github.com:Transparency010101/scrab-img-from-ligthshot.git
```

```
cd scrab-img-from-ligthshot/
```

Create virtual environment: 
```
python3 -m venv env 
```

Then activate(launch) virtual environment: 
- **Linux**: `source env/bin/activate`

```
python3 setup.py install
```
If occurred permision denied error:
```
sudo python3 setup.py install
```
## Usage

PyPi or Source:
```
silf -h
```

Poetry:
```
poetry run silf -h
```
When program finished, open the project's folder `img/`, and there will be images.

## Notes
Idea for the project I got [there](https://www.youtube.com/watch?v=OUki27mlwOw) 4:30.

I'm developing this project only for my practise, maybe there is fools ideas,
controversial points regarding the development, not serious thing, attitude towards whole development

P.S. Не бейте за англиский.
