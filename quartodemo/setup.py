from setuptools import setup, find_packages

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="quartodemo",
    version="0.1.0",
    author="Lus",
    author_email="your.email@example.com",
    description="Description of your package",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/XinyanYang95/QuartoCode",
    packages=find_packages(),
    install_requires=[
        "matplotlib",
        "numpy",
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)