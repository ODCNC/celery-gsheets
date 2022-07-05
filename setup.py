from setuptools import setup, find_packages

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="celery-gsheets",
    version="0.1.0",
    author="David Jeong",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/ODCNC/celery-gsheets",
    packages=["celery_gsheets"],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.8',
)
