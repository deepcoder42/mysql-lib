#!/usr/bin/python
# Classification (U)

"""Program:  server_reconnect.py

    Description:  Unit testing of Server.reconnect method in mysql_class.py.

    Usage:
        test/unit/mysql_class/server_reconnect.py

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
import mock

# Local
sys.path.append(os.getcwd())
import lib.machine as machine
import mysql_class
import version

__version__ = version.__version__


class UnitTest(unittest.TestCase):

    """Class:  UnitTest

    Description:  Class which is a representation of a unit testing.

    Methods:
        setUp -> Initialize testing environment.
        test_is_connected_false -> Test is_connected is False.

    """

    def setUp(self):

        """Function:  setUp

        Description:  Initialization for unit testing.

        Arguments:

        """

        self.name = "Mysql_Server"
        self.server_id = 10
        self.sql_user = "mysql_user"
        self.sql_pass = "my_japd"
        self.machine = getattr(machine, "Linux")()
        self.host = "host_server"
        self.port = 3307
        self.defaults_file = "def_cfg_file"
        self.extra_def_file = "extra_cfg_file"

    @mock.patch("mysql_class.Server.is_connected")
    def test_is_connected_true(self, mock_conn):

        """Function:  test_is_connected_true

        Description:  Test is_connected is True.

        Arguments:

        """

        mock_conn.return_value = True

        mysqldb = mysql_class.Server(
            self.name, self.server_id, self.sql_user, self.sql_pass,
            os_type=self.machine, defaults_file=self.defaults_file)

        self.assertFalse(mysqldb.reconnect())


if __name__ == "__main__":
    unittest.main()
