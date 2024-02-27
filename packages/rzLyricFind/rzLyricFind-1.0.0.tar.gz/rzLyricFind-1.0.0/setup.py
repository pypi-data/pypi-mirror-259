from setuptools import setup, find_packages
import codecs
import os

here = os.path.abspath(os.path.dirname(__file__))

with codecs.open(os.path.join(here, "README.md"), encoding="utf-8") as fh:
    long_description = "\n" + fh.read()

# This gets deployed when a new release is made by github actions
VERSION = '1.0.0'

# CHANGEME VARS
PACKAGE_NAME = "rzLyricFind"
DESCRIPTION = 'Easy Way To find lyric'
LONG_DESCRIPTION = 'Find Lyric Of Song easier, just type part of lyric'
AUTHOR_NAME = "Reza"
AUTHOR_EMAIL = "neobyteid@gmail.com"
PROJECT_URL = "https://github.com/indobyte/rzLyricFind"
REQUIRED_PACKAGES = ['bs4','requests','urllib3'] # required 3rd party tools used by your package
PROJECT_KEYWORDS = ['pypi', 'python', 'automation', 'cicd','lyricFind','rzLyricFind']
# Read more about classifiers at
# https://pypi.org/classifiers/
CLASSIFIERS = [
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows"]

setup(
    name=PACKAGE_NAME,
    version=VERSION,
    author=AUTHOR_NAME,
    author_email=AUTHOR_EMAIL,
    description=DESCRIPTION,
    url = PROJECT_URL,
    long_description_content_type="text/markdown",
    long_description=long_description,
    packages=find_packages(),
    install_requires=REQUIRED_PACKAGES,
    keywords=PROJECT_KEYWORDS,
    classifiers=CLASSIFIERS
)