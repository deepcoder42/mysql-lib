#!/usr/bin/python
# Classification (U)

"""Program:  slaverep_connect.py

    Description:  Unit testing of SlaveRep.connect method in mysql_class.py.

    Usage:
        test/unit/mysql_class/slaverep_connect.py

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
import mysql_class
import lib.machine as machine
import version

__version__ = version.__version__


class UnitTest(unittest.TestCase):

    """Class:  UnitTest

    Description:  Class which is a representation of a unit testing.

    Methods:
        setUp -> Initialize testing environment.
        test_db_up -> Test with connection up.
        test_db_down -> Test with connection down.

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

        self.mysqlrep = mysql_class.SlaveRep(
            self.name, self.server_id, self.sql_user, self.sql_pass,
            os_type=self.machine, defaults_file=self.defaults_file)

    @mock.patch("mysql_class.SlaveRep.upd_slv_status")
    @mock.patch("mysql_class.Server.set_srv_gtid")
    @mock.patch("mysql_class.Server.connect")
    def test_db_up(self, mock_conn, mock_set, mock_update):

        """Function:  test_db_up

        Description:  Test with connection up.

        Arguments:

        """

        mock_conn.return_value = True
        mock_set.return_value = True
        mock_update.return_value = True

        self.mysqlrep.conn = True

        self.assertFalse(self.mysqlrep.connect())

    @mock.patch("mysql_class.Server.connect")
    def test_db_down(self, mock_server):

        """Function:  test_db_down

        Description:  Test with connection down.

        Arguments:

        """

        mock_server.return_value = True

        self.assertFalse(self.mysqlrep.connect())


if __name__ == "__main__":
    unittest.main()
