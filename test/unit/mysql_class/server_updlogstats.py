#!/usr/bin/python
# Classification (U)

"""Program:  server_updlogstats.py

    Description:  Unit testing of Server.upd_log_stats in mysql_class.py.

    Usage:
        test/unit/mysql_class/server_updlogstats.py

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

        self.show_stat = [{"Position": "23678", "Binlog_Do_DB": None,
                           "File": "mysql-bin.01234",
                           "Binlog_Ignore_DB": "tempdb"}]

    @mock.patch("mysql_class.show_master_stat")
    def test_value(self, mock_stat):

        """Function:  test_value

        Description:  Test with values returned.

        Arguments:

        """

        mock_stat.return_value = self.show_stat
        mysqldb = mysql_class.Server(self.name, self.server_id, self.sql_user,
                                     self.sql_pass, self.machine,
                                     defaults_file=self.defaults_file)

        mysqldb.upd_log_stats()
        self.assertEqual((mysqldb.pos, mysqldb.do_db, mysqldb.file,
                          mysqldb.ign_db),
                         ("23678", None, "mysql-bin.01234", "tempdb"))


if __name__ == "__main__":
    unittest.main()
