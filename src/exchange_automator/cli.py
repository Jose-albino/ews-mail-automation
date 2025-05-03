import argparse
from my_package import __version__

def main():
    parser = argparse.ArgumentParser(description="My Package CLI")
    parser.add_argument("-v", "--version", action="store_true", help="Show version")
    args = parser.parse_args()

    if args.version:
        print(f"My Package version {__version__}")
    else:
        print("Hello from my_package!")
