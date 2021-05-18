#!/usr/bin/python
# Classification (U)

"""Program:  analyze_tbl.py

    Description:  Unit testing of analyze_tbl in mysql_libs.py.

    Usage:
        test/unit/mysql_libs/analyze_tbl.py

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
        sql -> Stub holder for Server.sql method.

    """

    def __init__(self):

        """Method:  __init__

        Description:  Class initialization.

        Arguments:

        """

        self.cmd = None

    def col_sql(self, cmd):

        """Method:  col_sql

        Description:  Stub holder for Server.col_sql method.

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
        test_analyze_tbl -> Test analyze_tbl function.

    """

    def setUp(self):

        """Function:  setUp

        Description:  Initialization for unit testing.

        Arguments:

        """

        self.server = Server()

    def test_analyze_tbl(self):

        """Function:  test_analyze_tbl

        Description:  Test analyze_tbl function.

        Arguments:

        """

        self.assertTrue(mysql_libs.analyze_tbl(self.server, "Db_name",
                                               "Tbl_name"))


if __name__ == "__main__":
    unittest.main()
