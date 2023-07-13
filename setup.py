from setuptools import setup

setup(
    name='silf',
    install_requires=["requests", "argparse", "bs4", "fake-useragent", "lxml"],
    entry_points={
        'console_scripts': [
            'silf = silf.main:main',
        ],
    }
)
