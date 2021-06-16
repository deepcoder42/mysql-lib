#!/usr/bin/python
# Classification (U)

"""Program:  server_fetchlogs.py

    Description:  Unit testing of Server.fetch_log in mysql_class.py.

    Usage:
        test/unit/mysql_class/server_fetchlogs.py

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
        test_fetch_logs_name -> Test with file name.
        test_fetch_logs_null -> Test with null file name.

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

    def test_fetch_logs_name(self):

        """Function:  test_fetch_logs_name

        Description:  Test with file name.

        Arguments:

        """

        mysqldb = mysql_class.Server(self.name, self.server_id, self.sql_user,
                                     self.sql_pass, self.machine,
                                     defaults_file=self.defaults_file)
        mysqldb.file = "File_Name"

        self.assertEqual(mysqldb.fetch_log(), "File_Name")

    @mock.patch("mysql_class.Server.upd_log_stats")
    def test_fetch_logs_null(self, mock_update):

        """Function:  test_fetch_logs_null

        Description:  Test with null file name.

        Arguments:

        """

        mock_update.return_value = True
        mysqldb = mysql_class.Server(self.name, self.server_id, self.sql_user,
                                     self.sql_pass, self.machine,
                                     defaults_file=self.defaults_file)

        self.assertEqual(mysqldb.fetch_log(), None)


if __name__ == "__main__":
    unittest.main()
