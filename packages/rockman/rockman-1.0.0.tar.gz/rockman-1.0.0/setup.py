from setuptools import setup, find_packages
import codecs
import os

here = os.path.abspath(os.path.dirname(__file__))

with codecs.open(os.path.join(here, "README.md"), encoding="utf-8") as fh:
    long_description = "\n" + fh.read()

VERSION = '1.0.0'
DESCRIPTION = 'automatic code generator using python'
LONG_DESCRIPTION = "long description of the package"

# Setting up
setup(
    name="rockman",
    version=VERSION,
    author="Jorge Hospinal Flores (Acid Jelly)",
    author_email="jhospinal@acidjelly.com",
    description=DESCRIPTION,
    long_description_content_type="text/markdown",  # Specify Markdown content type
    long_description=long_description,
    packages=find_packages(),
    install_requires=[],
    keywords=['python', 'react', 'django', 'redux', 'generator', 'code'],
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ]
)
