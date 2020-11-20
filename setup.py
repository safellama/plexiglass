import os
from setuptools import setup, find_packages

with open(os.path.join(os.path.dirname(__file__), 'version')) as f:
    version = f.read().strip()
setup(
    name="plexiglass",
    version=version,
    description="PyTorch toolbox for cybersecurity research and testing against adversarial attacks and deepfakes.",
    url="https://github.com/enochkan/plexiglass",
    author="Chi Nok Enoch Kan @chinokenochkan",
    author_email="kanxx030@gmail.com",
    packages=find_packages(),
)