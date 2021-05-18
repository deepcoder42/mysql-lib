#!/usr/bin/python
# Classification (U)

"""Program:  server_vert_sql.py

    Description:  Integration testing of Server.vert_sql in mysql_class.py.

    Usage:
        test/integration/mysql_class/server_vert_sql.py

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
        test_no_params -> Test with col_sql method with no params.
        test_params -> Test with params.

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
        self.cmd = "show global status like %s"
        self.cmd2 = "show global status"
        self.var = "uptime"

    def test_no_params(self):

        """Function:  test_no_params

        Description:  Test with col_sql method with no params.

        Arguments:

        """

        data = self.svr.vert_sql(self.cmd2)

        self.assertTrue(data["Uptime"] > 0)

    def test_params(self):

        """Function:  test_params

        Description:  Test with params.

        Arguments:

        """

        data = self.svr.vert_sql(self.cmd, (self.var,))

        self.assertTrue(data["Uptime"] > 0)


if __name__ == "__main__":
    unittest.main()
