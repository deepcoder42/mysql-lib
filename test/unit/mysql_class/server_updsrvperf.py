#!/usr/bin/python
# Classification (U)

"""Program:  server_updsrvperf.py

    Description:  Unit testing of Server.upd_srv_perf in mysql_class.py.

    Usage:
        test/unit/mysql_class/server_updsrvperf.py

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

        self.show_status = [
            {"Variable_name": "Innodb_buffer_pool_pages_free",
             "Value": "1"},
            {"Variable_name": "Innodb_buffer_pool_pages_data",
             "Value": "2"},
            {"Variable_name": "Innodb_buffer_pool_pages_total",
             "Value": "3"},
            {"Variable_name": "Innodb_buffer_pool_pages_dirty",
             "Value": "4"},
            {"Variable_name": "Max_used_connections",
             "Value": "5"},
            {"Variable_name": "Uptime_since_flush_status",
             "Value": "5"},
            {"Variable_name": "Binlog_cache_disk_use",
             "Value": "6"},
            {"Variable_name": "Binlog_cache_use",
             "Value": "7"},
            {"Variable_name": "Innodb_buffer_pool_wait_free",
             "Value": "8"},
            {"Variable_name": "Innodb_log_waits",
             "Value": "9"},
            {"Variable_name": "Innodb_row_lock_time_avg",
             "Value": "10"},
            {"Variable_name": "Innodb_row_lock_time_max",
             "Value": "11"},
            {"Variable_name": "Innodb_buffer_pool_reads",
             "Value": "12"},
            {"Variable_name": "Innodb_buffer_pool_read_requests",
             "Value": "13"},
            {"Variable_name": "Innodb_buffer_pool_read_ahead_evicted",
             "Value": "14"},
            {"Variable_name": "Innodb_buffer_pool_read_ahead",
             "Value": "15"},
            {"Variable_name": "Created_tmp_disk_tables",
             "Value": "16"}]

    @mock.patch("mysql_class.Server.col_sql")
    def test_value(self, mock_sql):

        """Function:  test_value

        Description:  Test with values returned.

        Arguments:

        """

        mock_sql.return_value = self.show_status
        mysqldb = mysql_class.Server(self.name, self.server_id, self.sql_user,
                                     self.sql_pass, self.machine,
                                     defaults_file=self.defaults_file)

        mysqldb.upd_srv_perf()

        self.assertEqual((mysqldb.indb_buf_free, mysqldb.binlog_tot,
                          mysqldb.indb_buf_evt_pct),
                         (1, 13, 93))


if __name__ == "__main__":
    unittest.main()
