from setuptools import setup

import os, glob

def read(fname):
    return open(fname).read()

setup(
    name = "pycisco",
    version = "0.0.1",
    author = "Marek Wiewiorski",
    author_email = "mwicat@gmail.com",
    description = ("Routines associates with Cisco VOIP phones"),
    license = "GPLv3",
    packages=['pycisco'],
    install_requires = ['plac'],
    long_description=read('README'),
    entry_points = {
        'console_scripts': [
            ]
        },


)
