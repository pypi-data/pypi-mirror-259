from setuptools import setup, find_packages
classifiers = [
    "Development Status :: 5 - Production/Stable",
    "Intended Audience :: Education",
    "Operating System :: MacOS",
    "License :: OSI Approved :: MIT License",
    "Programming Language :: Python :: 3"
]

setup(
    name="hello_ascii",
    version="0.0.1",
    description="a simple hello world with ascii",
    long_description=open("README.txt").read() + "\n\n" + open("CHANGELOG.txt").read(),
    long_description_content_type='text/markdown',
    url="",
    author="",
    author_email="",
    license="MIT",
    classifiers=classifiers,
    keywords="",
    packages=find_packages(),
)
