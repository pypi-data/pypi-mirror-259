# -*- coding: utf-8 -*-
import setuptools

with open("README.md", "r", encoding='utf-8') as fh:
    long_description = fh.read()


def get_requirements(fname):
    "Takes requirements from requirements.txt and returns a list."
    with open(fname) as fp:
        reqs = list()
        for lib in fp.read().split("\n"):
            # Ignore pypi flags and comments
            if not lib.startswith("-") or lib.startswith("#"):
                reqs.append(lib.strip())
        return reqs


install_requires = get_requirements("requirements.txt")

setuptools.setup(
    name="langloop",
    version="0.0.1",
    author="Jamie Alexandre",
    author_email="jamalex+python@gmail.com",
    description="LLM-Powered Human-in-the-Loop Processing Pipelines",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/jamalex/langloop",
    install_requires=install_requires,
    include_package_data=True,
    packages=setuptools.find_packages(),
    python_requires=">=3.8",
    license="GPL",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)",
        "Operating System :: OS Independent",
    ],
)
