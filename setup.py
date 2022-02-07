from setuptools import setup, find_packages

with open('requirements.txt') as f:
    requirements = f.read().splitlines()

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="celery-gsheets",
    version="0.0.1",
    author="David Jeong",
    author_email="hyjeong@odcnc.co.kr",
    description="A django-celery-beat package for gsheets",
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
    install_requires=requirements,
)
