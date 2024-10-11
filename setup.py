#! /usr/bin/env python
# -*- coding: utf-8 -*-

import os

from setuptools import find_packages, setup
from setuptools.command.install import install


class inst(install):
    def run(self):
        install.run(self)
        path = (
            os.getcwd().replace(" ", r"\ ").replace("(", r"\(").replace(")", r"\)")
            + "/bin/"
        )
        os.system("sh " + path + "install_teleservices_ideabox.sh")


version = "0.1"

setup(
    name="teleservices-ideabox",
    version=version,
    author="Nicolas Selva, Jordano Modesto",
    author_email="support-ts@imio.be",
    packages=find_packages(),
    include_package_data=True,
    install_requires=[],
    url="https://github.com/IMIO//teleservices-ideabox",
    classifiers=[
        "Development Status :: 2 - Pre-Alpha",
        "Environment :: Web Environment",
        "Framework :: Django",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: GNU Affero General Public License v3 or later (AGPLv3+)",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
    ],
    zip_safe=False,
    cmdclass={
        "inst": inst,
    },
)
