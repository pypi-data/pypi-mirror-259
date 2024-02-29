from setuptools import setup, find_packages
import codecs
import os

VERSION = '0.0.2'
DESCRIPTION = 'Log to table converter package'

# Setting up
setup(
    name="vanta_yc",
    version=VERSION,
    author="YC",
    author_email="<yatipa.c@vanta-capital.com>",
    description=DESCRIPTION,
    packages=find_packages(),
    install_requires=['pandas', 'datetime', 'decimal', 're'],
    keywords=['python', 'log', 'table', 'lob', 'mbp', 'onItch'],
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ]
)
