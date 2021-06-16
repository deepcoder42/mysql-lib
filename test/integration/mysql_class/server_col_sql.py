#!/usr/bin/python
# Classification (U)

"""Program:  server_col_sql.py

    Description:  Integration testing of Server.col_sql in mysql_class.py.

    Usage:
        test/integration/mysql_class/server_col_sql.py

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


class UnitTest(unittest.TestCase):

    """Class:  UnitTest

    Description:  Class which is a representation of a unit testing.

    Methods:
        setUp -> Initialize testing environment.
        test_col_sql2 -> Test with col_sql method.
        test_col_sql -> Test with col_sql method.

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
        self.svr.connect()
        self.cmd = "show databases"
        self.database = "mysql"

    def test_col_sql2(self):

        """Function:  test_col_sql2

        Description:  Test with col_sql method.

        Arguments:

        """

        data = self.svr.col_sql(self.cmd)

        self.assertTrue(isinstance(data, list))

    def test_col_sql(self):

        """Function:  test_col_sql

        Description:  Test with col_sql method.

        Arguments:

        """

        data = self.svr.col_sql(self.cmd)
        db_list = []

        for item in data:
            db_list.append(item["Database"])

        self.assertTrue(self.database in db_list)


if __name__ == "__main__":
    unittest.main()
