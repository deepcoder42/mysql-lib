# Classification (U)

"""Program:  setup.py

    Description:  A setuptools based setup module.

"""

# Libraries and Global Variables

# Standard
import os
import setuptools

# Third-party

# Local
import version


# Read in long description from README file.
here = os.path.abspath(os.path.dirname(__file__))

with open(os.path.join(here, "README.md")) as f_hdlr:
    LONG_DESCRIPTION = f_hdlr.read()

setuptools.setup(
    name="MySQL_Lib",
    description="MySQL classes and libraries to connect to MySQL Database.",
    author="deepcoder42",
    author_email="deepcoder42@gmail.com",
    url="https://github.com/deepcoder42/mysql-lib",
    version=version.__version__,
    platforms=["Linux"],
    long_description=LONG_DESCRIPTION,

    py_modules=[
        "mysql_class",
        "mysql_libs",
        "__init__",
        "version"],

    classifiers=[
        # Common Values:
        #  1 - Pre-Alpha
        #  2 - Alpha
        #  3 - Beta
        #  4 - Field
        #  5 - Production/Stable
        "Development Status :: 5 - Production/Stable",
        "Operating System :: Linux",
        "Operating System :: Linux :: Centos",
        "Operating System :: Linux :: Ubuntu",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2.6",
        "Programming Language :: Python :: 2.7",
        "Topic :: Database",
        "Topic :: Database :: MySQL :: 5.5",
        "Topic :: Database :: MySQL :: 5.6"])
