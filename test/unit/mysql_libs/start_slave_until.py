#!/usr/bin/python
# Classification (U)

"""Program:  start_slave_until.py

    Description:  Unit testing of start_slave_until in mysql_libs.py.

    Usage:
        test/unit/mysql_libs/start_slave_until.py

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

        self.gtid_mode = "Yes"
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
        test_fail -> Test failure option.
        test_gtid -> Test with gtid mode.
        test_non_gtid -> Test with non-gtid mode.

    """

    def setUp(self):

        """Function:  setUp

        Description:  Initialization for unit testing.

        Arguments:

        """

        self.server = Server()

    def test_fail(self):

        """Function:  test_fail

        Description:  Test failure option.

        Arguments:

        """

        self.assertEqual(
            mysql_libs.start_slave_until(self.server),
            (True, "One of the arguments is missing."))

    def test_gtid(self):

        """Function:  test_gtid

        Description:  Test with gtid mode.

        Arguments:

        """

        self.assertEqual(
            mysql_libs.start_slave_until(
                self.server, gtid=12345, stop_pos="before"), (False, None))

    def test_non_gtid(self):

        """Function:  test_non_gtid

        Description:  Test with non-gtid mode.

        Arguments:

        """

        self.assertEqual(
            mysql_libs.start_slave_until(
                self.server, log_file="Filename", log_pos=12345),
            (False, None))


if __name__ == "__main__":
    unittest.main()
