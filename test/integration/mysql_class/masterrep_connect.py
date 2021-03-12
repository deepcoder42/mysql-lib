#!/usr/bin/python
# Classification (U)

"""Program:  masterrep_connect.py

    Description:  Integration testing of MasterRep.connect in mysql_class.py.

    Usage:
        test/integration/mysql_class/masterrep_connect.py

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
        test_silent_true2 -> Test with silent true set.
        test_silent_true -> Test with silent true set.
        test_silent_false2 -> Test with silent false set.
        test_silent_false -> Test with silent false set.
        test_silent_default2 -> Test with silent default setting.
        test_silent_default -> Test with silent default setting.
        test_exe_gtid -> Test with exe_gtid attribute.
        test_gtid_mode -> Test with gtid_mode attribute.
        test_config -> Test with config attribute.
        test_connect_exception -> Test connection method exception.
        test_connect -> Test connect method.

    """

    def setUp(self):

        """Function:  setUp

        Description:  Initialization for unit testing.

        Arguments:

        """

        self.base_dir = "test/integration"
        self.config_dir = os.path.join(self.base_dir, "config")
        self.config_name = "master_mysql_cfg"
        self.cfg = gen_libs.load_module(self.config_name, self.config_dir)
        self.svr = mysql_class.MasterRep(
            self.cfg.name, self.cfg.sid, self.cfg.user, self.cfg.japd,
            os_type=getattr(machine, self.cfg.serv_os)(), host=self.cfg.host,
            port=self.cfg.port, defaults_file=self.cfg.cfg_file)
        self.svr2 = mysql_class.MasterRep(
            self.cfg.name, self.cfg.sid, self.cfg.user, "testmenopwd",
            os_type=getattr(machine, self.cfg.serv_os)(), host=self.cfg.host,
            port=self.cfg.port, defaults_file=self.cfg.cfg_file)
        self.err_msg = "Couldn't connect to database.  MySQL error 1045:"

    def test_silent_true2(self):

        """Function:  test_silent_true2

        Description:  Test with silent true set.

        Arguments:

        """

        self.svr2.connect(silent=True)

        self.assertEqual(self.svr2.conn_msg[:48], self.err_msg)

    def test_silent_true(self):

        """Function:  test_silent_true

        Description:  Test with silent true set.

        Arguments:

        """

        self.svr2.connect(silent=True)

        self.assertFalse(self.svr2.conn)

    def test_silent_false2(self):

        """Function:  test_silent_false2

        Description:  Test with silent false set.

        Arguments:

        """

        with gen_libs.no_std_out():
            self.svr2.connect(silent=False)

        self.assertEqual(self.svr2.conn_msg[:48], self.err_msg)

    def test_silent_false(self):

        """Function:  test_silent_false

        Description:  Test with silent false set.

        Arguments:

        """

        with gen_libs.no_std_out():
            self.svr2.connect(silent=False)

        self.assertFalse(self.svr2.conn)

    def test_silent_default2(self):

        """Function:  test_silent_default2

        Description:  Test with silent default setting.

        Arguments:

        """

        with gen_libs.no_std_out():
            self.svr2.connect()

        self.assertEqual(self.svr2.conn_msg[:48], self.err_msg)

    def test_silent_default(self):

        """Function:  test_silent_default

        Description:  Test with silent default setting.

        Arguments:

        """

        with gen_libs.no_std_out():
            self.svr2.connect()

        self.assertFalse(self.svr2.conn)

    def test_exe_gtid(self):

        """Function:  test_exe_gtid

        Description:  Test with exe_gtid attribute.

        Arguments:

        """

        self.svr.connect()

        self.assertTrue(self.svr.exe_gtid)

    def test_gtid_mode(self):

        """Function:  test_gtid_mode

        Description:  Test with gtid_mode attribute.

        Arguments:

        """

        self.svr.connect()

        self.assertTrue(self.svr.gtid_mode)

    def test_config(self):

        """Function:  test_config

        Description:  Test with config attribute.

        Arguments:

        """

        self.svr.connect()

        self.assertTrue(self.svr.config)

    def test_connect_exception(self):

        """Function:  test_connect_exception

        Description:  Test connection method exception.

        Arguments:

        """

        with gen_libs.no_std_out():
            self.svr2.connect()

        self.assertFalse(self.svr2.conn)

    def test_connect(self):

        """Function:  test_connect

        Description:  Test connect method.

        Arguments:

        """

        self.svr.connect()

        self.assertTrue(self.svr.conn)


if __name__ == "__main__":
    unittest.main()
