#!/usr/bin/python
# Classification (U)

"""Program:  server_upd_srv_perf.py

    Description:  Integration testing of Server.upd_srv_perf in mysql_class.py.

    Usage:
        test/integration/mysql_class/server_upd_srv_perf.py

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
        test_pool_write -> Test with Innodb_buffer_pool_write_requests attr.
        test_secondary_attr -> Test with secondary attribute.
        test_base_attr -> Test with base attribute.

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

    def test_pool_write(self):

        """Function:  test_pool_write

        Description:  Test with Innodb_buffer_pool_write_requests attr.

        Arguments:

        """

        self.svr.upd_srv_perf()

        self.assertTrue(self.svr.indb_buf_write >= 0)

    def test_secondary_attr(self):

        """Function:  test_secondary_attr

        Description:  Test with secondary attribute.

        Arguments:

        """

        self.svr.upd_srv_perf()

        self.assertTrue(self.svr.binlog_tot >= 0)

    def test_base_attr(self):

        """Function:  test_base_attr

        Description:  Test with base attribute.

        Arguments:

        """

        self.svr.upd_srv_perf()

        self.assertTrue(self.svr.max_use_conn >= 0)


if __name__ == "__main__":
    unittest.main()
