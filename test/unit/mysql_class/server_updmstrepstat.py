#!/usr/bin/python
# Classification (U)

"""Program:  server_updmstrepstat.py

    Description:  Unit testing of Server.upd_mst_rep_stat in mysql_class.py.

    Usage:
        test/unit/mysql_class/server_updmstrepstat.py

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
        test_version2 -> Test with innodb_support_xa in pre-MySQL 8.0.
        test_version -> Test with no innodb_support_xa in MySQL 8.0.
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
        self.fetch_vars = [{"log_bin": "ON"}, {"sync_binlog": "YES"},
                           {"innodb_flush_log_at_trx_commit": "YES"},
                           {"innodb_support_xa": "ON"},
                           {"binlog_format": "BIN"}]
        self.fetch_vars2 = [{"log_bin": "ON"}, {"sync_binlog": "YES"},
                            {"innodb_flush_log_at_trx_commit": "YES"},
                            {},
                            {"binlog_format": "BIN"}]

    @mock.patch("mysql_class.fetch_sys_var")
    def test_version2(self, mock_sysvar):

        """Function:  test_version2

        Description:  Test with innodb_support_xa in pre-MySQL 8.0.

        Arguments:

        """

        mock_sysvar.side_effect = self.fetch_vars
        mysqldb = mysql_class.Server(self.name, self.server_id, self.sql_user,
                                     self.sql_pass, self.machine,
                                     defaults_file=self.defaults_file)

        mysqldb.upd_mst_rep_stat()
        self.assertEqual(mysqldb.innodb_xa, "ON")

    @mock.patch("mysql_class.fetch_sys_var")
    def test_version(self, mock_sysvar):

        """Function:  test_version

        Description:  Test with no innodb_support_xa in MySQL 8.0.

        Arguments:

        """

        mock_sysvar.side_effect = self.fetch_vars2
        mysqldb = mysql_class.Server(self.name, self.server_id, self.sql_user,
                                     self.sql_pass, self.machine,
                                     defaults_file=self.defaults_file)

        mysqldb.upd_mst_rep_stat()
        self.assertEqual(mysqldb.innodb_xa, None)

    @mock.patch("mysql_class.fetch_sys_var")
    def test_value(self, mock_sysvar):

        """Function:  test_value

        Description:  Test with values returned.

        Arguments:

        """

        mock_sysvar.side_effect = self.fetch_vars
        mysqldb = mysql_class.Server(self.name, self.server_id, self.sql_user,
                                     self.sql_pass, self.machine,
                                     defaults_file=self.defaults_file)

        mysqldb.upd_mst_rep_stat()
        self.assertEqual((mysqldb.log_bin, mysqldb.log_format), ("ON", "BIN"))


if __name__ == "__main__":
    unittest.main()
