import os
import setuptools
from setuptools import find_packages, setup

with open(os.path.join(os.path.dirname(__file__), "README.md")) as readme:
    README = readme.read()

setuptools.setup(
    name="fcs-core-model-engine",
    version='0.1.0',
    author="Tamas Balogh",
    author_email="info@femsolve.com",
    description="Python bound methods to FCS.Core.ModelEngine libraries.",
    long_description="Python bound methods to FCS.Core.ModelEngine libraries.",
    long_description_content_type="text/markdown",
    include_package_data=True,
    url="https://github.com/Femsolve-Engineering/FCS.Core.ModelEngine.PyAPI",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: Microsoft :: Windows"
    ],
    extras_require={
        "dev" : ["pytest>=7.0", "twine>=4.0.2"]
    },
    python_requires='==3.11',
)