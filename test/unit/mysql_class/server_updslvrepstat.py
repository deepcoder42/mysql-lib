#!/usr/bin/python
# Classification (U)

"""Program:  server_updslvrepstat.py

    Description:  Unit testing of Server.upd_slv_rep_stat in mysql_class.py.

    Usage:
        test/unit/mysql_class/server_updslvrepstat.py

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
        test_value -> Test with values returned.

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

    @mock.patch("mysql_class.fetch_sys_var")
    def test_value(self, mock_sysvar):

        """Function:  test_value

        Description:  Test with values returned.

        Arguments:

        """

        mock_sysvar.side_effect = [{"log_bin": "ON"},
                                   {"read_only": "YES"},
                                   {"log_slave_updates": "YES"},
                                   {"sync_master_info": "NO"},
                                   {"sync_relay_log": "ON"},
                                   {"sync_relay_log_info": "YES"}]
        mysqldb = mysql_class.Server(self.name, self.server_id, self.sql_user,
                                     self.sql_pass, self.machine,
                                     defaults_file=self.defaults_file)

        mysqldb.upd_slv_rep_stat()

        self.assertEqual((mysqldb.log_bin, mysqldb.sync_rly_info),
                         ("ON", "YES"))


if __name__ == "__main__":
    unittest.main()
