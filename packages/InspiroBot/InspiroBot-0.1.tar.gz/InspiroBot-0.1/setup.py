from setuptools import setup, find_packages

setup(
    name="InspiroBot",
    version="0.1",
    author="masswyn",
    author_email="maswwyn24@gmail.com",
    description="A web application for generating random motivational affirmations and inspiring quotes.",
    url="https://github.com/maswwyn/InspiroBot",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
