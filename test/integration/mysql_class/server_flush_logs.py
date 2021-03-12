#!/usr/bin/python
# Classification (U)

"""Program:  server_flush_logs.py

    Description:  Integration testing of Server.flush_logs in
        mysql_class.py.

    Usage:
        test/integration/mysql_class/server_flush_logs.py

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
        test_base2 -> Test with base attribute.
        test_base -> Test with base attribute.

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

    def test_base2(self):

        """Function:  test_base2

        Description:  Test with base attribute.

        Arguments:

        """

        self.svr.upd_log_stats()
        fname = self.svr.file
        self.svr.flush_logs()

        self.assertTrue(self.svr.file != fname)

    def test_base(self):

        """Function:  test_base

        Description:  Test with base attribute.

        Arguments:

        """

        self.svr.flush_logs()

        self.assertTrue(self.svr.pos)


if __name__ == "__main__":
    unittest.main()
