import os

from setuptools import find_packages, setup

with open(os.path.join(os.path.dirname(__file__), "plexiglass/version")) as f:
    version = f.read().strip()
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
