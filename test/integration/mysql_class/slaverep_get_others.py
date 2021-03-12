#!/usr/bin/python
# Classification (U)

"""Program:  slaverep_get_others.py

    Description:  Integration testing of SlaveRep.get_others in
        mysql_class.py.

    Usage:
        test/integration/mysql_class/slaverep_get_others.py

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
        test_retry -> Test with retry attribute.
        test_tmp_tbl -> Test with tmp_tbl attribute.
        test_skip_ctr -> Test with skip_ctr attribute.

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

    def test_retry(self):

        """Function:  test_retry

        Description:  Test with retry attribute.

        Arguments:

        """

        data = self.svr.get_others()

        self.assertTrue(data[2] or data[2] == "")

    def test_tmp_tbl(self):

        """Function:  test_tmp_tbl

        Description:  Test with tmp_tbl attribute.

        Arguments:

        """

        data = self.svr.get_others()

        self.assertTrue(data[1] or data[1] == "")

    def test_skip_ctr(self):

        """Function:  test_skip_ctr

        Description:  Test with skip_ctr attribute.

        Arguments:

        """

        data = self.svr.get_others()

        self.assertTrue(data[0] or data[0] == 0)


if __name__ == "__main__":
    unittest.main()
