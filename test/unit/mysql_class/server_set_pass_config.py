#!/usr/bin/python
# Classification (U)

"""Program:  server_set_pass_config.py

    Description:  Unit testing of Server.set_pass_config method in
        mysql_class.py.

    Usage:
        test/unit/mysql_class/server_set_pass_config.py

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

# Local
sys.path.append(os.getcwd())
import mysql_class
import lib.machine as machine
import version

__version__ = version.__version__

# Global
KEY1 = "pass"
KEY2 = "wd"


class UnitTest(unittest.TestCase):

    """Class:  UnitTest

    Description:  Class which is a representation of a unit testing.

    Methods:
        setUp -> Initialize testing environment.
        test_set_pass_config -> Test setting configuration settings.

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
        self.new_sql_pass = "my_japd2"

    def test_set_pass_config(self):

        """Function:  test_set_pass_config

        Description:  Test setting configuration settings.

        Arguments:

        """

        global KEY1
        global KEY2

        new_config = {KEY1 + KEY2: self.new_sql_pass}

        mysqldb = mysql_class.Server(
            self.name, self.server_id, self.sql_user, self.sql_pass,
            os_type=self.machine, defaults_file=self.defaults_file)
        mysqldb.set_pass_config(self.new_sql_pass)

        self.assertEqual((mysqldb.config, mysqldb.sql_pass),
                         (new_config, self.new_sql_pass))


if __name__ == "__main__":
    unittest.main()
