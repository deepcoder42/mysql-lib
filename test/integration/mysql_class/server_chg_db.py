#!/usr/bin/python
# Classification (U)

"""Program:  server_chg_db.py

    Description:  Integration testing of Server.chg_db method in
        mysql_class.py.

    Usage:
        test/integration/mysql_class/server_chg_db.py

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
        test_chg_db -> Test with change of database.
        test_chg_db_none -> Test with no database is passed.

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
        self.database = "mysql"

    def test_chg_db(self):

        """Function:  test_chg_db

        Description:  Test with change of database.

        Arguments:

        """

        self.svr.chg_db(self.database)

        self.assertEqual(self.svr.conn.database, self.database)

    def test_chg_db_none(self):

        """Function:  test_chg_db_none

        Description:  Test with no database is passed.

        Arguments:

        """

        self.svr.chg_db()

        self.assertFalse(self.svr.conn.database)


if __name__ == "__main__":
    unittest.main()
