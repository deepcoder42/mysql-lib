#!/usr/bin/python
# Classification (U)

"""Program:  server_set_pass_config.py

    Description:  Integration testing of Server.set_pass_config method in
        mysql_class.py.

    Usage:
        test/integration/mysql_class/server_set_pass_config.py

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
import lib.gen_libs as gen_libs
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

        self.base_dir = "test/integration"
        self.config_dir = os.path.join(self.base_dir, "config")
        self.config_name = "mysql_cfg"
        cfg = gen_libs.load_module(self.config_name, self.config_dir)
        self.svr = mysql_class.Server(
            cfg.name, cfg.sid, cfg.user, cfg.japd,
            os_type=getattr(machine, cfg.serv_os)(), host=cfg.host,
            port=cfg.port, defaults_file=cfg.cfg_file)
        self.new_sql_pass = "my_japd2"

    def test_set_pass_config(self):

        """Function:  test_set_pass_config

        Description:  Test setting configuration settings.

        Arguments:

        """

        global KEY1
        global KEY2

        new_config = {KEY1 + KEY2: self.new_sql_pass}

        self.svr.set_pass_config(self.new_sql_pass)

        self.assertEqual((self.svr.config, self.svr.sql_pass),
                         (new_config, self.new_sql_pass))


if __name__ == "__main__":
    unittest.main()
