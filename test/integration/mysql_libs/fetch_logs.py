#!/usr/bin/python
# Classification (U)

"""Program:  fetch_logs.py

    Description:  Integration testing of fetch_logs in mysql_libs.py.

    Note:  This test assumes binary logs is enabled in the MySQL database.

    Usage:
        test/integration/mysql_libs/fetch_logs.py

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
        test_fetch_logs -> Test fetch_logs function.

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

    def test_fetch_logs(self):

        """Function:  test_fetch_logs

        Description:  Test fetch_logs function.

        Arguments:

        """

        data = mysql_libs.fetch_logs(self.svr)

        self.assertTrue(data[0]["Log_name"])


if __name__ == "__main__":
    unittest.main()
