#!/usr/bin/python
# Classification (U)

"""Program:  optimize_tbl.py

    Description:  Unit testing of optimize_tbl in mysql_libs.py.

    Usage:
        test/unit/mysql_libs/optimize_tbl.py

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
        col_sql -> Stub holder for mysql_class.Server.col_sql method.

    """

    def __init__(self):

        """Method:  __init__

        Description:  Class initialization.

        Arguments:

        """

        self.cmd = None

    def col_sql(self, cmd):

        """Method:  col_sql

        Description:  Stub holder for mysql_class.Server.col_sql method.

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
        test_optimize_tbl -> Test optimize_tbl function.

    """

    def setUp(self):

        """Function:  setUp

        Description:  Initialization for unit testing.

        Arguments:

        """

        self.server = Server()

    def test_optimize_tbl(self):

        """Function:  test_optimize_tbl

        Description:  Test optimize_tbl function.

        Arguments:

        """

        self.assertTrue(mysql_libs.optimize_tbl(self.server, "Dbname",
                                                "Tblname"))


if __name__ == "__main__":
    unittest.main()
