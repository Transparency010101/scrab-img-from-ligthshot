from setuptools import setup, find_packages

setup(
    name='scrab_img_from_ligthshot',
    version='2.2.0',
    description="scrab images from ligthshot (i don't know is this legal)",
    url="https://github.com/Transparency010101/scrab-img-from-ligthshot",
    install_requires=[
        'requests',
        'argparse',
        'beautifulsoup4',
        "fake-useragent",
        "lxml"
    ],
    entry_points={
        'console_scripts': [
            'silf = silf:main',
        ]
    },
)
