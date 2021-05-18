#!/usr/bin/python
# Classification (U)

"""Program:  fetch_global_var.py

    Description:  Unit testing of fetch_global_var in mysql_class.py.

    Usage:
        test/unit/mysql_class/fetch_global_var.py

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
import mysql_class
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
        self.var = None

    def vert_sql(self, cmd, var):

        """Method:  vert_sql

        Description:  Stub holder for Server.vert_sql method.

        Arguments:
            (input) cmd -> Query command.
            (input) var -> Global variable name.

        """

        self.cmd = cmd
        self.var = var

        return True


class UnitTest(unittest.TestCase):

    """Class:  UnitTest

    Description:  Class which is a representation of a unit testing.

    Methods:
        setUp -> Initialize testing environment.
        test_fetch_global_var -> Test fetch_global_var function.

    """

    def setUp(self):

        """Function:  setUp

        Description:  Initialization for unit testing.

        Arguments:

        """

        self.server = Server()

    def test_fetch_global_var(self):

        """Function:  test_fetch_global_var

        Description:  Test fetch_global_var function.

        Arguments:

        """

        self.assertTrue(mysql_class.fetch_global_var(self.server, "Variable"))


if __name__ == "__main__":
    unittest.main()
