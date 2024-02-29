import os
import setuptools
from setuptools import find_packages, setup

with open(os.path.join(os.path.dirname(__file__), "README.md")) as readme:
    README = readme.read()

setuptools.setup(
    name="fcs-core-model-engine",
    version='0.1.1',
    author="Tamas Balogh",
    author_email="info@femsolve.com",
    description="Python bound methods to FCS.Core.ModelEngine libraries.",
    long_description="Python bound methods to FCS.Core.ModelEngine libraries.",
    long_description_content_type="text/markdown",
    url="https://github.com/Femsolve-Engineering/FCS.Core.ModelEngine.PyAPI",
    classifiers=[
        "Programming Language :: Python :: 3.11",
        "License :: OSI Approved :: MIT License",
        "Operating System :: Microsoft :: Windows"
    ],
    extras_require={
        "dev" : ["pytest>=7.0", "twine>=4.0.2"]
    },
    # Include package data, specifying the relative path to the binaries
    # package_data={
    #     'fcscore_package': ['*.pyd', '*.so', '*.dll'],
    # },
    include_package_data=True,
    python_requires='==3.11',
)