# -*- coding: utf-8 -*-
from setuptools import setup, find_packages


setup(
    name='instainf',
    version="1.26",
    packages=find_packages(),
    author="casterix",
    install_requires=["argparse","requests","phonenumbers","pycountry"],
    description="A tool to get all probable informtation from a user's instagram account",
    long_description="It is a tool written to retrieve private information such as User ID, Bio, Phone Number, Mail Address from Instagram accounts via API.",
    include_package_data=True,
    url='http://github.com/casterix193/instainf',
    entry_points = {'console_scripts': ['instainf = instainf.core:main']},
    classifiers=[
        "Programming Language :: Python",
        "License :: MIT License",
    ],
)
