import argparse

from exchange_automator import __version__

description = "Exchange Automator"


def main()->None:
    parser = argparse.ArgumentParser(description=description)
    parser.add_argument("-v", "--version", action="store_true", help="Show version")
    args = parser.parse_args()

    if args.version:
        print(f"Version is v{__version__}")
    else:
        print(description)
