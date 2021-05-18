#!/usr/bin/python
# Classification (U)

"""Program:  reset_slave.py

    Description:  Unit testing of reset_slave in mysql_libs.py.

    Usage:
        test/unit/mysql_libs/reset_slave.py

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
        cmd_sql -> Stub holder for mysql_class.Server.cmd_sql method.

    """

    def __init__(self):

        """Method:  __init__

        Description:  Class initialization.

        Arguments:

        """

        self.cmd = None

    def cmd_sql(self, cmd):

        """Method:  cmd_sql

        Description:  Stub holder for mysql_class.Server.cmd_sql method.

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
        test_reset_slave -> Test reset_slave function.

    """

    def setUp(self):

        """Function:  setUp

        Description:  Initialization for unit testing.

        Arguments:

        """

        self.server = Server()

    def test_reset_slave(self):

        """Function:  test_reset_slave

        Description:  Test reset_slave function.

        Arguments:

        """

        self.assertFalse(mysql_libs.reset_slave(self.server))


if __name__ == "__main__":
    unittest.main()
