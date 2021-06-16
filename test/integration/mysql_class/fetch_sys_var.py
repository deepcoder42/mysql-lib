#!/usr/bin/python
# Classification (U)

"""Program:  fetch_sys_var.py

    Description:  Integration testing of fetch_sys_var in mysql_class.py.

    Usage:
        test/Integration/mysql_class/fetch_sys_var.py

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
        test_fetch_session -> Test with session level variable.
        test_fetch_default -> Test with level variable.

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

    def test_fetch_global(self):

        """Function:  test_fetch_session

        Description:  Test with session level variable.

        Arguments:

        """

        data = mysql_class.fetch_sys_var(self.svr, "wait_timeout",
                                         level="global")
        self.assertTrue(data["wait_timeout"] >= 0)

    def test_fetch_session(self):

        """Function:  test_fetch_session

        Description:  Test with session level variable.

        Arguments:

        """

        data = mysql_class.fetch_sys_var(self.svr, "warning_count",
                                         level="session")
        self.assertTrue(data["warning_count"] >= 0)

    def test_fetch_default(self):

        """Function:  test_fetch_default

        Description:  Test with level variable.

        Arguments:

        """

        data = mysql_class.fetch_sys_var(self.svr, "warning_count")
        self.assertTrue(data["warning_count"] >= 0)


if __name__ == "__main__":
    unittest.main()
