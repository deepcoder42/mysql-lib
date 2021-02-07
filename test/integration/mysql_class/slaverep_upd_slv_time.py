#!/usr/bin/python
# Classification (U)

"""Program:  slaverep_upd_slv_time.py

    Description:  Integration testing of SlaveRep.upd_slv_time in
        mysql_class.py.

    Usage:
        test/integration/mysql_class/slaverep_upd_slv_time.py

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
        test_upd_slv_time -> Test upd_slv_time method.

    """

    def setUp(self):

        """Function:  setUp

        Description:  Initialization for unit testing.

        Arguments:

        """

        self.base_dir = "test/integration"
        self.config_dir = os.path.join(self.base_dir, "config")
        self.config_name = "slave_mysql_cfg"
        self.cfg = gen_libs.load_module(self.config_name, self.config_dir)
        self.svr = mysql_class.SlaveRep(
            self.cfg.name, self.cfg.sid, self.cfg.user, self.cfg.japd,
            os_type=getattr(machine, self.cfg.serv_os)(), host=self.cfg.host,
            port=self.cfg.port, defaults_file=self.cfg.cfg_file)
        self.svr.connect()

    def test_upd_slv_time(self):

        """Function:  test_upd_slv_time

        Description:  Test upd_slv_time method.

        Arguments:

        """

        self.svr.upd_slv_status()
        data = self.svr.secs_behind
        self.svr.upd_slv_time()

        self.assertTrue(self.svr.secs_behind == data)


if __name__ == "__main__":
    unittest.main()
