#!/usr/bin/python
# Classification (U)

"""Program:  slaverep_updslvtime.py

    Description:  Unit testing of SlaveRep.upd_slv_time in mysql_class.py.

    Usage:
        test/unit/mysql_class/slaverep_updslvtime.py

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
        test_none_secsbehind -> Test None for Seconds_Behind_Master.
        test_int_secsbehind -> Test integer for Seconds_Behind_Master.
        test_string_secsbehind -> Test string for Seconds_Behind_Master.
        test_except_secsbehind -> Test raising exception: Seconds_Behind_Master
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

        self.show_stat = [{"Seconds_Behind_Master": "10"}]

    @mock.patch("mysql_class.show_slave_stat")
    def test_none_secsbehind(self, mock_stat):

        """Function:  test_none_secsbehind

        Description:  Test None for Seconds_Behind_Master.

        Arguments:

        """

        self.show_stat[0]["Seconds_Behind_Master"] = None

        mock_stat.return_value = self.show_stat
        mysqlrep = mysql_class.SlaveRep(self.name, self.server_id,
                                        self.sql_user, self.sql_pass,
                                        self.machine,
                                        defaults_file=self.defaults_file)

        mysqlrep.upd_slv_time()
        self.assertEqual(mysqlrep.secs_behind, None)

    @mock.patch("mysql_class.show_slave_stat")
    def test_int_secsbehind(self, mock_stat):

        """Function:  test_int_secsbehind

        Description:  Test integer for Seconds_Behind_Master.

        Arguments:

        """

        self.show_stat[0]["Seconds_Behind_Master"] = 10

        mock_stat.return_value = self.show_stat
        mysqlrep = mysql_class.SlaveRep(self.name, self.server_id,
                                        self.sql_user, self.sql_pass,
                                        self.machine,
                                        defaults_file=self.defaults_file)

        mysqlrep.upd_slv_time()
        self.assertEqual(mysqlrep.secs_behind, 10)

    @mock.patch("mysql_class.show_slave_stat")
    def test_string_secsbehind(self, mock_stat):

        """Function:  test_string_secsbehind

        Description:  Test string for Seconds_Behind_Master.

        Arguments:

        """

        mock_stat.return_value = self.show_stat
        mysqlrep = mysql_class.SlaveRep(self.name, self.server_id,
                                        self.sql_user, self.sql_pass,
                                        self.machine,
                                        defaults_file=self.defaults_file)

        mysqlrep.upd_slv_time()
        self.assertEqual(mysqlrep.secs_behind, 10)

    @mock.patch("mysql_class.show_slave_stat")
    def test_except_secsbehind(self, mock_stat):

        """Function:  test_except_secsbehind

        Description:  Test raising exception for Seconds_Behind_Master.

        Arguments:

        """

        mock_stat.return_value = self.show_stat
        mysqlrep = mysql_class.SlaveRep(self.name, self.server_id,
                                        self.sql_user, self.sql_pass,
                                        self.machine,
                                        defaults_file=self.defaults_file)

        mysqlrep.upd_slv_time()
        self.assertEqual(mysqlrep.secs_behind, 10)

    @mock.patch("mysql_class.show_slave_stat")
    def test_value(self, mock_stat):

        """Function:  test_value

        Description:  Test with values returned.

        Arguments:

        """

        mock_stat.return_value = self.show_stat
        mysqlrep = mysql_class.SlaveRep(self.name, self.server_id,
                                        self.sql_user, self.sql_pass,
                                        self.machine,
                                        defaults_file=self.defaults_file)

        mysqlrep.upd_slv_time()
        self.assertEqual(mysqlrep.secs_behind, 10)


if __name__ == "__main__":
    unittest.main()
