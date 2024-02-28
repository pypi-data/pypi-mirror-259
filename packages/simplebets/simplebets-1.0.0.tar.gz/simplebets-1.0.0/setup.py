import os
from setuptools import find_namespace_packages, setup

base_path = os.path.abspath(os.path.dirname(__file__))

version = "1.0.0"

setup(
    name="simplebets",
    version=version,
    author="Jarrod McCarthy",
    description="Same Game Multi Engine",
    url="https://github.com/JarrodMccarthy/SimpleBets.git",
    platforms="any",
    packages=[p for p in find_namespace_packages(where=base_path) if p.startswith("simplebets")],
    classifiers=[
        "License :: Other/Proprietary License",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
    ],
    zip_safe = True,
    install_requires = [
        "trueskill==0.4.5",
        "pandas==2.1.3"
    ]
)