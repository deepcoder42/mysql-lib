#!/usr/bin/python
# Classification (U)

"""Program:  show_slave_stat.py

    Description:  Integration testing of show_slave_stat in mysql_class.py.

    Usage:
        test/integration/mysql_class/show_slave_stat.py

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
        test_show_slave_stat2 -> Test show_slave_stat function.
        test_show_slave_stat -> Test show_slave_stat function.

    """

    def setUp(self):

        """Function:  setUp

        Description:  Initialization for unit testing.

        Arguments:

        """

        self.base_dir = "test/integration"
        self.config_dir = os.path.join(self.base_dir, "config")
        self.config_name = "slave_mysql_cfg"
        cfg = gen_libs.load_module(self.config_name, self.config_dir)
        self.svr = mysql_class.SlaveRep(
            cfg.name, cfg.sid, cfg.user, cfg.japd,
            os_type=getattr(machine, cfg.serv_os)(), host=cfg.host,
            port=cfg.port, defaults_file=cfg.cfg_file)
        self.svr.connect()

    def test_show_slave_stat2(self):

        """Function:  test_show_slave_stat2

        Description:  Test show_slave_stat function.

        Arguments:

        """

        data = mysql_class.show_slave_stat(self.svr)

        self.assertTrue(data and data[0]["Master_UUID"])

    def test_show_slave_stat(self):

        """Function:  test_show_slave_stat

        Description:  Test show_slave_stat function.

        Arguments:

        """

        data = mysql_class.show_slave_stat(self.svr)

        self.assertTrue(isinstance(data, list))


if __name__ == "__main__":
    unittest.main()
