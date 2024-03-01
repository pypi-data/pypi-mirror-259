from setuptools import setup, find_packages
import codecs
import os

here = os.path.abspath(os.path.dirname(__file__))

with codecs.open(os.path.join(here, "README.md"), encoding="utf-8") as fh:
    long_description = "\n" + fh.read()

VERSION = '0.0.1'
DESCRIPTION = 'ReproCipher is a Python package designed to provide consistent encryption.'
LONG_DESCRIPTION = 'ReproCipher is a Python package designed to provide consistent encryption.'

# Setting up
setup(
    name="reprocipher",
    version=VERSION,
    author="Ravindu Priyankara",
    author_email="<mail@neuralnine.com>",
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    long_description=long_description,
    install_requires = [],
    packages=find_packages(),
    keywords=['python', 'encryption', 'Deterministic cryptography', 'Fixed seed randomness', 'Consistent encryption output', 'Reliable cryptographic operations','Predictable encryption behavior','Testable encryption','Audit-friendly cryptography'],
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ]
)