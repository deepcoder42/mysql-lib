#!/usr/bin/python
# Classification (U)

"""Program:  masterrep_updmststatus.py

    Description:  Unit testing of MasterRep.upd_mst_status in mysql_class.py.

    Usage:
        test/unit/mysql_class/masterrep_updmststatus.py

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

        self.show_stat = [{"Executed_Gtid_Set": "23678"}]

    @mock.patch("mysql_class.Server.upd_log_stats")
    @mock.patch("mysql_class.show_master_stat")
    def test_value(self, mock_stat, mock_log):

        """Function:  test_value

        Description:  Test with values returned.

        Arguments:

        """

        mock_log.return_value = True
        mock_stat.return_value = self.show_stat
        mysqldb = mysql_class.MasterRep(self.name, self.server_id,
                                        self.sql_user, self.sql_pass,
                                        self.machine,
                                        defaults_file=self.defaults_file)

        mysqldb.upd_mst_status()
        self.assertEqual((mysqldb.exe_gtid), ("23678"))


if __name__ == "__main__":
    unittest.main()
