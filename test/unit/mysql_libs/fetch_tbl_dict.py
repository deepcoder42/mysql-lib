#!/usr/bin/python
# Classification (U)

"""Program:  fetch_tbl_dict.py

    Description:  Unit testing of fetch_tbl_dict in mysql_libs.py.

    Usage:
        test/unit/mysql_libs/fetch_tbl_dict.py

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
        sql -> Stub holder for mysql_class.Server.sql method.

    """

    def __init__(self):

        """Method:  __init__

        Description:  Class initialization.

        Arguments:

        """

        self.qry = None

    def col_sql(self, qry):

        """Method:  col_sql

        Description:  Stub holder for mysql_class.Server.col_sql method.

        Arguments:
            (input) qry -> Query command.

        """

        self.qry = qry

        return True


class UnitTest(unittest.TestCase):

    """Class:  UnitTest

    Description:  Class which is a representation of a unit testing.

    Methods:
        setUp -> Initialize testing environment.
        test_fetch_tbl_dict -> Test fetch_tbl_dict function.

    """

    def setUp(self):

        """Function:  setUp

        Description:  Initialization for unit testing.

        Arguments:

        """

        self.server = Server()

    def test_fetch_tbl_dict(self):

        """Function:  test_fetch_tbl_dict

        Description:  Test fetch_tbl_dict function.

        Arguments:

        """

        self.assertTrue(mysql_libs.fetch_tbl_dict(self.server, "Dbname"))


if __name__ == "__main__":
    unittest.main()
