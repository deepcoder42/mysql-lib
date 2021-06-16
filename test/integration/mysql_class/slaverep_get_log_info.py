#!/usr/bin/python
# Classification (U)

"""Program:  slaverep_get_log_info.py

    Description:  Integration testing of SlaveRep.get_log_info in
        mysql_class.py.

    Usage:
        test/integration/mysql_class/slaverep_get_log_info.py

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
        test_exec_mst_pos -> Test with exec_mst_pos attribute.
        test_mst_read_pos -> Test with mst_read_pos attribute.
        test_relay_mst_log -> Test with relay_mst_log attribute.
        test_mst_log -> Test with mst_log attribute.

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

    def test_exec_mst_pos(self):

        """Function:  test_exec_mst_pos

        Description:  Test with exec_mst_pos attribute.

        Arguments:

        """

        data = self.svr.get_log_info()

        self.assertTrue(data[3])

    def test_mst_read_pos(self):

        """Function:  test_mst_read_pos

        Description:  Test with mst_read_pos attribute.

        Arguments:

        """

        data = self.svr.get_log_info()

        self.assertTrue(data[2])

    def test_relay_mst_log(self):

        """Function:  test_relay_mst_log

        Description:  Test with relay_mst_log attribute.

        Arguments:

        """

        data = self.svr.get_log_info()

        self.assertTrue(data[1])

    def test_mst_log(self):

        """Function:  test_mst_log

        Description:  Test with mst_log attribute.

        Arguments:

        """

        data = self.svr.get_log_info()

        self.assertTrue(data[0])


if __name__ == "__main__":
    unittest.main()
