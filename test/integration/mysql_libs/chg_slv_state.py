#!/usr/bin/python
# Classification (U)

"""Program:  chg_slv_state.py

    Description:  Integration testing of chg_slv_state in mysql_libs.py.

    Usage:
        test/integration/mysql_libs/chg_slv_state.py

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
import mysql_libs
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
        test_non_option -> Test with a non-option.
        test_start_slaves2 -> Test start option with already started slaves.
        test_start_slaves -> Test with start option.
        test_stop_slaves2 -> Test with stop option on stopped slaves.
        test_stop_slaves -> Test with stop option.
        tearDown -> Clean up of testing environment.

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
        self.status = False

    def test_non_option(self):

        """Function:  test_non_option

        Description:  Test with a non-option.

        Arguments:

        """

        self.svr.upd_slv_status()

        if self.svr.is_slv_running():
            with gen_libs.no_std_out():
                mysql_libs.chg_slv_state([self.svr], "status")
            self.svr.upd_slv_status()

            self.assertTrue(self.svr.is_slv_running())

        else:
            self.assertTrue(self.status)

    def test_start_slaves2(self):

        """Function:  test_start_slaves2

        Description:  Test with start option with already started slaves.

        Arguments:

        """

        self.svr.upd_slv_status()

        if self.svr.is_slv_running():
            mysql_libs.chg_slv_state([self.svr], "start")
            self.svr.upd_slv_status()

            self.assertTrue(self.svr.is_slv_running())

        else:
            self.assertTrue(self.status)

    def test_start_slaves(self):

        """Function:  test_start_slaves

        Description:  Test with start option.

        Arguments:

        """

        self.svr.stop_slave()
        self.svr.upd_slv_status()

        if self.svr.is_slv_running():
            self.assertTrue(self.status)

        else:
            mysql_libs.chg_slv_state([self.svr], "start")
            self.svr.upd_slv_status()

            self.assertTrue(self.svr.is_slv_running())

    def test_stop_slaves2(self):

        """Function:  test_stop_slaves2

        Description:  Test with stop option on stopped slaves.

        Arguments:

        """

        self.svr.stop_slave()
        self.svr.upd_slv_status()

        if self.svr.is_slv_running():
            self.assertTrue(self.status)

        else:
            mysql_libs.chg_slv_state([self.svr], "stop")
            self.svr.upd_slv_status()

            self.assertFalse(self.svr.is_slv_running())

    def test_stop_slaves(self):

        """Function:  test_stop_slaves

        Description:  Test with stop option.

        Arguments:

        """

        self.svr.upd_slv_status()

        if self.svr.is_slv_running():
            mysql_libs.chg_slv_state([self.svr], "stop")
            self.svr.upd_slv_status()

            self.assertFalse(self.svr.is_slv_running())

        else:
            self.assertTrue(self.status)

    def tearDown(self):

        """Function:  tearDown

        Description:  Clean up of testing environment.

        Arguments:

        """

        self.svr.start_slave()


if __name__ == "__main__":
    unittest.main()
