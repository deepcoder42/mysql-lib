#!/usr/bin/python
# Classification (U)

"""Program:  change_master_to.py

    Description:  Unit testing of change_master_to in mysql_libs.py.

    Usage:
        test/unit/mysql_libs/change_master_to.py

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
import lib.gen_libs as gen_libs
import mysql_libs
import version

__version__ = version.__version__


class Server(object):

    """Class:  Server

    Description:  Class stub holder for Server class.

    Methods:
        __init__ -> Class initialization.
        cmd_sql -> Stub holder for Server.cmd_sql method.

    """

    def __init__(self):

        """Method:  __init__

        Description:  Class initialization.

        Arguments:

        """

        self.gtid_mode = True
        self.host = "hostname"
        self.port = 3306
        self.sql_user = "sqluser"
        self.sql_pass = "japd"
        self.file = "binlog-filename"
        self.pos = "file-position"
        self.name = "server-name"
        self.rep_user = "rep_user"
        self.rep_japd = "rep_japd"
        self.cmd = None

    def cmd_sql(self, cmd):

        """Method:  cmd_sql

        Description:  Stub holder for Server.cmd_sql method.

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
        test_change_master_to_non_gtid -> Test in gtid_mode off.
        test_change_master_to_gtid -> Test in gtid_mode on.

    """

    def setUp(self):

        """Function:  setUp

        Description:  Initialization for unit testing.

        Arguments:

        """

        self.master = Server()
        self.slave = Server()

    def test_change_master_to_non_gtid(self):

        """Function:  test_change_master_to_non_gtid

        Description:  Test in gtid_mode off.

        Arguments:

        """

        self.master.gtid_mode = None

        with gen_libs.no_std_out():
            self.assertFalse(mysql_libs.change_master_to(self.master,
                                                         self.slave))

    def test_change_master_to_gtid(self):

        """Function:  test_change_master_to_gtid

        Description:  Test in gtid_mode on.

        Arguments:

        """

        with gen_libs.no_std_out():
            self.assertFalse(mysql_libs.change_master_to(self.master,
                                                         self.slave))


if __name__ == "__main__":
    unittest.main()
