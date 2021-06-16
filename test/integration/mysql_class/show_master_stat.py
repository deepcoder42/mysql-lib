#!/usr/bin/python
# Classification (U)

"""Program:  show_master_stat.py

    Description:  Integration testing of show_master_stat in mysql_class.py.

    Usage:
        test/integration/mysql_class/show_master_stat.py

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
        test_show_master_stat2 -> Test show_master_stat function.
        test_show_master_stat -> Test show_master_stat function.

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

    def test_show_master_stat2(self):

        """Function:  test_show_master_stat2

        Description:  Test show_master_stat function.

        Arguments:

        """

        data = mysql_class.show_master_stat(self.svr)

        self.assertTrue(data[0]["File"])

    def test_show_master_stat(self):

        """Function:  test_show_master_stat

        Description:  Test show_master_stat function.

        Arguments:

        """

        data = mysql_class.show_master_stat(self.svr)

        self.assertTrue(data[0]["Position"] > 0)


if __name__ == "__main__":
    unittest.main()
