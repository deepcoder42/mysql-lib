#!/usr/bin/python
# Classification (U)

"""Program:  fetch_logs.py

    Description:  Unit testing of fetch_logs in mysql_libs.py.

    Usage:
        test/unit/mysql_libs/fetch_logs.py

    Arguments:

"""

# Libraries and Global Variables

# Standard
import sys
import os

if sys.version_info < (2, 7):
    import unittest2 as unittest
else:
    import unittest

# Third-party

# Local
sys.path.append(os.getcwd())
import mysql_libs
import version

__version__ = version.__version__


class Server(object):

    """Class:  Server

    Description:  Class stub holder for Server class.

    Methods:
        __init__ -> Class initialization.
        col_sql -> col_sql method.

    """

    def __init__(self):

        """Method:  __init__

        Description:  Class initialization.

        Arguments:

        """

        self.cmd = None

    def col_sql(self, cmd):

        """Method:  col_sql

        Description:  col_sql method.

        Arguments:
            (input) cmd -> Query command.

        """

        self.cmd = cmd

        return True


class UnitTest(unittest.TestCase):

    """Class:  UnitTest

    Description:  Class which is a representation of a unit testing.

    Methods:
        setUp -> Initialize testing environment.
        test_fetch_logs -> Test fetch_logs function.

    """

    def setUp(self):

        """Function:  setUp

        Description:  Initialization for unit testing.

        Arguments:

        """

        self.server = Server()

    def test_fetch_logs(self):

        """Function:  test_fetch_logs

        Description:  Test fetch_logs function.

        Arguments:

        """

        self.assertTrue(mysql_libs.fetch_logs(self.server))


if __name__ == "__main__":
    unittest.main()
