#!/usr/bin/python
# Classification (U)

"""Program:  slaverep_get_err_stat.py

    Description:  Integration testing of SlaveRep.get_err_stat in
        mysql_class.py.

    Usage:
        test/integration/mysql_class/slaverep_get_err_stat.py

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
        test_sql_err_time -> Test with sql_err_time attribute.
        test_io_err_time -> Test with io_err_time attribute.
        test_sql_msg -> Test with sql_msg attribute.
        test_io_msg -> Test with io_msg attribute.
        test_sql_err -> Test with sql_err attribute.
        test_io_err -> Test with io_err attribute.

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

    def test_sql_err_time(self):

        """Function:  test_sql_err_time

        Description:  Test with sql_err_time attribute.

        Arguments:

        """

        data = self.svr.get_err_stat()

        self.assertTrue(data[5] or data[5] == "")

    def test_io_err_time(self):

        """Function:  test_io_err_time

        Description:  Test with io_err_time attribute.

        Arguments:

        """

        data = self.svr.get_err_stat()

        self.assertTrue(data[4] or data[4] == "")

    def test_sql_msg(self):

        """Function:  test_sql_msg

        Description:  Test with sql_msg attribute.

        Arguments:

        """

        data = self.svr.get_err_stat()

        self.assertTrue(data[3] or data[3] == "")

    def test_io_msgs(self):

        """Function:  test_io_msg

        Description:  Test with io_msg attribute.

        Arguments:

        """

        data = self.svr.get_err_stat()

        self.assertTrue(data[2] or data[2] == "")

    def test_sql_err(self):

        """Function:  test_sql_err

        Description:  Test with sql_err attribute.

        Arguments:

        """

        data = self.svr.get_err_stat()

        self.assertTrue(data[1] or data[1] == 0)

    def test_io_err(self):

        """Function:  test_io_err

        Description:  Test with io_err attribute.

        Arguments:

        """

        data = self.svr.get_err_stat()

        self.assertTrue(data[0] or data[0] == 0)


if __name__ == "__main__":
    unittest.main()
