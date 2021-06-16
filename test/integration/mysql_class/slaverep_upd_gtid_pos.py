#!/usr/bin/python
# Classification (U)

"""Program:  slaverep_upd_gtid_pos.py

    Description:  Integration testing of SlaveRep.upd_gtid_pos in
        mysql_class.py.

    Usage:
        test/integration/mysql_class/slaverep_upd_gtid_pos.py

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
        test_gtid_mode -> Test with GTID mode.
        test_gtid_pos -> Test with GTID positions.

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

    def test_gtid_mode(self):

        """Function:  test_gtid_mode

        Description:  Test with GTID mode.

        Arguments:

        """

        data1 = "%s" % self.svr.purged_gtidset
        self.svr.connect()
        self.svr.upd_gtid_pos()
        data1a = "%s" % self.svr.purged_gtidset

        if self.svr.gtid_mode:
            self.assertTrue(data1 != data1a)

        else:
            self.assertEqual(data1, data1a)

    def test_gtid_pos(self):

        """Function:  test_gtid_pos

        Description:  Test with GTID positions.

        Arguments:

        """

        data1 = "%s" % self.svr.retrieved_gtidset
        data2 = "%s" % self.svr.exe_gtidset
        self.svr.connect()
        self.svr.upd_gtid_pos()
        data1a = "%s" % self.svr.retrieved_gtidset
        data2a = "%s" % self.svr.exe_gtidset

        self.assertTrue(data1 != data1a and data2 != data2a)


if __name__ == "__main__":
    unittest.main()
