from .colors import bcolors

def colorfy(string: str, color: str = "OKBLUE"):
    """
    Pretty print a string with a color.
    """
    return f"{bcolors.__dict__[color]}{string}{bcolors.ENDC}"