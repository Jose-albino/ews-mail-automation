from setuptools import setup, find_packages

setup(
    name="exchange_automator",
    version="0.1.0",
    description="A CLI-enabled Python package",
    author="Jose Albino",
    author_email="pypi-packages-email.pendant519@passmail.com",
    packages=find_packages(),
    install_requires=[],
    entry_points={
        "console_scripts": [
            "exchange_automator=exchange_automator.cli:main"
        ]
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
    ],
)
