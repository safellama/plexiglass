from .colors import bcolors
import os, datetime
from subprocess import run

def colorfy(string: str, color: str = "OKBLUE"):
    """
    Pretty print a string with a color.
    """
    return f"{bcolors.__dict__[color]}{string}{bcolors.ENDC}"

def get_version(version):
    if "PYPI_RELEASE" not in os.environ:
        today = datetime.date.today()
        version = f"{version}.dev{today.year}{today.month}{today.day}"

        if "DEV_RELEASE" not in os.environ:
            git_hash = (
                run(
                    "git rev-parse --short HEAD".split(),
                    capture_output=True,
                    check=True,
                )
                .stdout.strip()
                .decode()
            )
            version = f"{version}+{git_hash}"

    return version