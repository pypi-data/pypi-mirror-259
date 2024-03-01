from setuptools import find_packages, setup

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="aperyon_greeter",
    version="3.1.3",
    author="Your Name",
    author_email="your@email.com",
    description="A simple package to greet people",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/your_username/simple_greeter",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
