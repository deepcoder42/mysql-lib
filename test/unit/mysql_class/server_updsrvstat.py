#!/usr/bin/python
# Classification (U)

"""Program:  server_updsrvstat.py

    Description:  Unit testing of Server.upd_srv_stat in mysql_class.py.

    Usage:
        test/unit/mysql_class/server_updsrvstat.py

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
        test_version -> Test with version pre MySQL 8.0.
        test_value2 -> Test with smaller tmp_tbl size.
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
        self.version = (5, 7, 33)
        self.version2 = (8, 0, 3)

        self.show_status = [
            {"Variable_name": "key_buffer_size",
             "Value": "10000000"},
            {"Variable_name": "innodb_buffer_pool_size",
             "Value": "2"},
            {"Variable_name": "innodb_additional_mem_pool_size",
             "Value": "3"},
            {"Variable_name": "innodb_log_buffer_size",
             "Value": "4"},
            {"Variable_name": "query_cache_size",
             "Value": "5"},
            {"Variable_name": "read_buffer_size",
             "Value": "5"},
            {"Variable_name": "read_rnd_buffer_size",
             "Value": "6"},
            {"Variable_name": "sort_buffer_size",
             "Value": "7"},
            {"Variable_name": "join_buffer_size",
             "Value": "8"},
            {"Variable_name": "thread_stack",
             "Value": "9"},
            {"Variable_name": "max_allowed_packet",
             "Value": "10"},
            {"Variable_name": "net_buffer_length",
             "Value": "11"},
            {"Variable_name": "max_connections",
             "Value": "12"},
            {"Variable_name": "max_heap_table_size",
             "Value": "13"},
            {"Variable_name": "tmp_table_size",
             "Value": "14"}]
        self.show_status2 = [
            {"Variable_name": "key_buffer_size",
             "Value": "10000000"},
            {"Variable_name": "innodb_buffer_pool_size",
             "Value": "2"},
            {"Variable_name": "innodb_additional_mem_pool_size",
             "Value": "3"},
            {"Variable_name": "innodb_log_buffer_size",
             "Value": "4"},
            {"Variable_name": "query_cache_size",
             "Value": "5"},
            {"Variable_name": "read_buffer_size",
             "Value": "5"},
            {"Variable_name": "read_rnd_buffer_size",
             "Value": "6"},
            {"Variable_name": "sort_buffer_size",
             "Value": "7"},
            {"Variable_name": "join_buffer_size",
             "Value": "8"},
            {"Variable_name": "thread_stack",
             "Value": "9"},
            {"Variable_name": "max_allowed_packet",
             "Value": "10"},
            {"Variable_name": "net_buffer_length",
             "Value": "11"},
            {"Variable_name": "max_connections",
             "Value": "12"},
            {"Variable_name": "max_heap_table_size",
             "Value": "13"},
            {"Variable_name": "tmp_table_size",
             "Value": "4"}]
        self.show_status3 = [
            {"Variable_name": "key_buffer_size",
             "Value": "10000000"},
            {"Variable_name": "innodb_buffer_pool_size",
             "Value": "2"},
            {"Variable_name": "innodb_additional_mem_pool_size",
             "Value": "3"},
            {"Variable_name": "innodb_log_buffer_size",
             "Value": "4"},
            {"Variable_name": "read_buffer_size",
             "Value": "5"},
            {"Variable_name": "read_rnd_buffer_size",
             "Value": "6"},
            {"Variable_name": "sort_buffer_size",
             "Value": "7"},
            {"Variable_name": "join_buffer_size",
             "Value": "8"},
            {"Variable_name": "thread_stack",
             "Value": "9"},
            {"Variable_name": "max_allowed_packet",
             "Value": "10"},
            {"Variable_name": "net_buffer_length",
             "Value": "11"},
            {"Variable_name": "max_connections",
             "Value": "12"},
            {"Variable_name": "max_heap_table_size",
             "Value": "13"},
            {"Variable_name": "tmp_table_size",
             "Value": "14"}]

    @mock.patch("mysql_class.fetch_global_var")
    @mock.patch("mysql_class.Server.col_sql")
    def test_version2(self, mock_sql, mock_var):

        """Function:  test_version2

        Description:  Test with version for MySQL 8.0 or higher.

        Arguments:

        """

        mock_var.side_effect = [{"Threads_connected": "15"},
                                {"Uptime": "16"}]
        mock_sql.return_value = self.show_status3
        mysqldb = mysql_class.Server(self.name, self.server_id, self.sql_user,
                                     self.sql_pass, self.machine,
                                     defaults_file=self.defaults_file)
        mysqldb.version = self.version2
        mysqldb.upd_srv_stat()

        self.assertEqual((mysqldb.version, mysqldb.qry_cache),
                         (self.version2, 0))

    @mock.patch("mysql_class.fetch_global_var")
    @mock.patch("mysql_class.Server.col_sql")
    def test_version(self, mock_sql, mock_var):

        """Function:  test_version

        Description:  Test with version pre MySQL 8.0.

        Arguments:

        """

        mock_var.side_effect = [{"Threads_connected": "15"},
                                {"Uptime": "16"}]
        mock_sql.return_value = self.show_status
        mysqldb = mysql_class.Server(self.name, self.server_id, self.sql_user,
                                     self.sql_pass, self.machine,
                                     defaults_file=self.defaults_file)
        mysqldb.version = self.version
        mysqldb.upd_srv_stat()

        self.assertEqual((mysqldb.version, mysqldb.qry_cache),
                         (self.version, 5))

    @mock.patch("mysql_class.fetch_global_var")
    @mock.patch("mysql_class.Server.col_sql")
    def test_value2(self, mock_sql, mock_var):

        """Function:  test_value2

        Description:  Test with smaller tmp_tbl size.

        Arguments:

        """

        mock_var.side_effect = [{"Threads_connected": "15"},
                                {"Uptime": "16"}]
        mock_sql.return_value = self.show_status2
        mysqldb = mysql_class.Server(self.name, self.server_id, self.sql_user,
                                     self.sql_pass, self.machine,
                                     defaults_file=self.defaults_file)
        mysqldb.version = self.version
        mysqldb.upd_srv_stat()

        self.assertEqual((mysqldb.buf_size, mysqldb.cur_conn, mysqldb.thr_mem,
                          mysqldb.tmp_tbl_size, mysqldb.prct_mem),
                         (10000000, 15, 56, 13, 100))

    @mock.patch("mysql_class.fetch_global_var")
    @mock.patch("mysql_class.Server.col_sql")
    def test_value(self, mock_sql, mock_var):

        """Function:  test_value

        Description:  Test with values returned.

        Arguments:

        """

        mock_var.side_effect = [{"Threads_connected": "15"},
                                {"Uptime": "16"}]
        mock_sql.return_value = self.show_status
        mysqldb = mysql_class.Server(self.name, self.server_id, self.sql_user,
                                     self.sql_pass, self.machine,
                                     defaults_file=self.defaults_file)
        mysqldb.version = self.version
        mysqldb.upd_srv_stat()

        self.assertEqual((mysqldb.buf_size, mysqldb.cur_conn, mysqldb.thr_mem,
                          mysqldb.tmp_tbl_size, mysqldb.prct_mem),
                         (10000000, 15, 56, 14, 100))


if __name__ == "__main__":
    unittest.main()
