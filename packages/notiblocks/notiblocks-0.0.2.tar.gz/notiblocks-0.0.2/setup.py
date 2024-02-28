from setuptools import setup, find_packages

VERSION = '0.0.2'
DESCRIPTION = 'Logging library for the impatient'

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

# Setting up
setup(
    name="notiblocks",
    version=VERSION,
    author="D4rkC47 (Deyan Sirakov)",
    author_email="dvs_sec@proton.me",
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    long_description=long_description,
    packages=find_packages(),
    install_requires=[],
    keywords=['python', 'logging', 'warning', 'terminal', 'ansi', 'color'],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent"
    ]
)