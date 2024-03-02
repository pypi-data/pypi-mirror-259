# setup.py
from setuptools import setup, find_packages

setup(
    name="upowwallet",
    version="3",
    packages=find_packages(),
    install_requires=[
        "asttokens==2.4.1",
        "base58==0.2.5",
        "certifi==2023.11.17",
        "charset-normalizer==2.0.12",
        " colorama==0.4.6",
        "executing==2.0.1",
        "fastecdsa==2.3.0",
        "icecream==2.1.3",
        "idna==3.6",
        "pygments==2.17.2",
        "requests==2.26.0",
        "six==1.16.0",
        "urllib3==1.26.18",
        "pickleDB~=0.9.2",
    ],
    author="upow",
    author_email="contact@upow.ai",
    description="A brief description of your package",
    long_description="A brief description of your package",
    long_description_content_type="text/markdown",
    url="https://github.com/yourusername/mypackage",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.9.9",
)
