import codecs
import io
import os
import re
import sys
import webbrowser
import platform
import configparser


try:
    from setuptools import setup,find_packages,Extension
except:
    from distutils.core import setup

if sys.version_info.major != 3 or sys.version_info.minor not in [5, 6, 7, 8, 9]:
    print('wrong version, should be 3.5/3.6/3.7/3.8 version')
    sys.exit()

with io.open('BaoFangRisk/__init__.py', 'rt', encoding='utf8') as f:
    context = f.read()
    VERSION = re.search(r'__version__ = \'(.*?)\'', context).group(1)
    AUTHOR = re.search(r'__author__ = \'(.*?)\'', context).group(1)


def read(fname):
    return codecs.open(os.path.join(os.path.dirname(__file__), fname)).read()


NAME = "BaoFangRisk"
PACKAGES = find_packages()
DESCRIPTION = "BaoFangRisk: performance attribution and optimizer tool based on Barra"
AUTHOR_EMAIL = "625180414@qq.com"
URL = ""
LICENSE = "MIT"
with open('requirements.txt') as reqs_file:
    INSTALL_REQUIRES = reqs_file.readlines()
setup(
    name=NAME,
    version=VERSION,
    description=DESCRIPTION,
    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
    ],
    install_requires=INSTALL_REQUIRES,
    author=AUTHOR,
    author_email=AUTHOR_EMAIL,
    url=URL,
    license=LICENSE,
    packages=PACKAGES,
    include_package_data=True,
    zip_safe=True
)
