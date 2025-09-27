from setuptools import setup, find_packages

setup(
    name="cheese",             # package name
    version="0.1.0",           # version
    packages=find_packages(),  # automatically finds cheese/
    install_requires=[],       # any dependencies
    description="A small cheese module",
    author="fela14",
    author_email="k.fakeye@yahoo.com",
    license="GPLv3"
    url="https://github.com/fela14/Cheese",  # repo URL
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.10',
)
