#!/usr/bin/python
# Classification (U)

"""Program:  masterrep_upd_mst_status.py

    Description:  Integration testing of MasterRep.upd_mst_status in
        mysql_class.py.

    Usage:
        test/integration/mysql_class/masterrep_upd_mst_status.py

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
        test_upd_mst_status -> Test upd_mst_status method.

    """

    def setUp(self):

        """Function:  setUp

        Description:  Initialization for unit testing.

        Arguments:

        """

        self.base_dir = "test/integration"
        self.config_dir = os.path.join(self.base_dir, "config")
        self.config_name = "master_mysql_cfg"
        cfg = gen_libs.load_module(self.config_name, self.config_dir)
        self.svr = mysql_class.MasterRep(
            cfg.name, cfg.sid, cfg.user, cfg.japd,
            os_type=getattr(machine, cfg.serv_os)(), host=cfg.host,
            port=cfg.port, defaults_file=cfg.cfg_file)
        self.svr.connect()

    def test_upd_mst_status(self):

        """Function:  test_upd_mst_status

        Description:  Test upd_mst_status method.

        Arguments:

        """

        self.svr.upd_mst_status()

        self.assertTrue(self.svr.exe_gtid)


if __name__ == "__main__":
    unittest.main()
