import os

from setuptools import find_packages, setup

with open(os.path.join(os.path.dirname(__file__), "plexiglass/version")) as f:
    version = f.read().strip()

import ast
import os
import re
import shutil
from distutils.command.build_scripts import build_scripts as _build_scripts
from distutils.util import convert_path, get_platform
from pathlib import Path

# type: ignore
# setuptools must be imported before distutils
import setuptools
from setuptools.command.develop import develop as _develop

with open("./README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="plexiglass",
    version=version,
    description="PyTorch toolbox for cybersecurity research and testing against adversarial attacks and deepfakes.",
    url="https://github.com/enochkan/plexiglass",
    author="Chi Nok Enoch Kan @chinokenochkan",
    install_requires=["torch>=1.7.0"],
    include_package_data=True,
    packages=find_packages(),
)
