#!/usr/bin/python
# Classification (U)

"""Program:  slaverep_updgtidpos.py

    Description:  Unit testing of SlaveRep.upd_gtid_pos in mysql_class.py.

    Usage:
        test/unit/mysql_class/slaverep_updgtidpos.py

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
        test_gtid_mode -> Test with gtid_mode set to True.
        test_value -> Test with values returned.

    """

    def setUp(self):

        """Function:  setUp

        Description:  Initialization for unit testing.

        Arguments:

        """

        self.gtidset1 = "35588520:333217-740055"
        self.gtidset2 = "35588520:333217-740045"
        self.name = "Mysql_Server"
        self.server_id = 10
        self.sql_user = "mysql_user"
        self.sql_pass = "my_japd"
        self.machine = getattr(machine, "Linux")()
        self.host = "host_server"
        self.port = 3307
        self.defaults_file = "def_cfg_file"
        self.extra_def_file = "extra_cfg_file"

        self.show_stat = [{"Retrieved_Gtid_Set": self.gtidset1,
                           "Executed_Gtid_Set": self.gtidset2}]

    @mock.patch("mysql_class.fetch_sys_var")
    @mock.patch("mysql_class.show_slave_stat")
    def test_gtid_mode(self, mock_stat, mock_var):

        """Function:  test_gtid_mode

        Description:  Test with gtid_mode set to True.

        Arguments:

        """

        mock_stat.return_value = self.show_stat
        mock_var.return_value = {"gtid_purged": "35588520:333220-333227"}
        mysqlrep = mysql_class.SlaveRep(self.name, self.server_id,
                                        self.sql_user, self.sql_pass,
                                        self.machine,
                                        defaults_file=self.defaults_file)
        mysqlrep.gtid_mode = True

        mysqlrep.upd_gtid_pos()
        self.assertEqual((str(mysqlrep.retrieved_gtidset),
                          str(mysqlrep.exe_gtidset),
                          str(mysqlrep.purged_gtidset)),
                         (self.gtidset1, self.gtidset2,
                          "35588520:333220-333227"))

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

        mysqlrep.upd_gtid_pos()
        self.assertEqual((str(mysqlrep.retrieved_gtidset),
                          str(mysqlrep.exe_gtidset),
                          str(mysqlrep.purged_gtidset)),
                         (self.gtidset1, self.gtidset2,
                          "None"))


if __name__ == "__main__":
    unittest.main()
