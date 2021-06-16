#!/usr/bin/python
# Classification (U)

"""Program:  is_cfg_valid.py

    Description:  Integration testing of is_cfg_valid in mysql_libs.py.

    Note:  This assumes the extra_def_file setting was set.

    Usage:
        test/integration/mysql_libs/is_cfg_valid.py

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
        test_multi_both_fail -> Test with multiple servers with both failed.
        test_multi_one_fail -> Test with multiple servers with one failed.
        test_multi_servers -> Test with multiple servers valid.
        test_chk_fails -> Test with check file fails.
        test_cfg_valid -> Test with extra cfg file is valid.

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
            port=cfg.port, defaults_file=cfg.cfg_file,
            extra_def_file=cfg.extra_def_file)
        self.svr2 = mysql_class.Server(
            cfg.name, cfg.sid, cfg.user, cfg.japd,
            os_type=getattr(machine, cfg.serv_os)(), host=cfg.host,
            port=cfg.port, defaults_file=cfg.cfg_file)
        self.msg = [self.svr2.name + ":  extra_def_file is not set."]
        self.svr3 = mysql_class.Server(
            cfg.name, cfg.sid, cfg.user, cfg.japd,
            os_type=getattr(machine, cfg.serv_os)(), host=cfg.host,
            port=cfg.port, defaults_file=cfg.cfg_file,
            extra_def_file=cfg.extra_def_file)
        self.svr4 = mysql_class.Server(
            cfg.name, cfg.sid, cfg.user, cfg.japd,
            os_type=getattr(machine, cfg.serv_os)(), host=cfg.host,
            port=cfg.port, defaults_file=cfg.cfg_file)
        self.msg2 = list(self.msg)
        self.msg2.append(self.svr4.name + ":  extra_def_file is not set.")

    def test_multi_both_fail(self):

        """Function:  test_multi_both_fail

        Description:  Test with multiple servers with both failed.

        Arguments:

        """

        self.assertEqual(mysql_libs.is_cfg_valid([self.svr2, self.svr4]),
                         (False, self.msg2))

    def test_multi_one_fail(self):

        """Function:  test_multi_one_fail

        Description:  Test with multiple servers with one failed.

        Arguments:

        """

        self.assertEqual(mysql_libs.is_cfg_valid([self.svr, self.svr2]),
                         (False, self.msg))

    def test_multi_servers(self):

        """Function:  test_multi_servers

        Description:  Test with multiple servers valid.

        Arguments:

        """

        self.assertEqual(mysql_libs.is_cfg_valid([self.svr, self.svr3]),
                         (True, []))

    def test_chk_fails(self):

        """Function:  test_chk_fails

        Description:  Test with check file fails.

        Arguments:

        """

        self.assertEqual(mysql_libs.is_cfg_valid([self.svr2]),
                         (False, self.msg))

    def test_cfg_valid(self):

        """Function:  test_cfg_valid

        Description:  Test with extra cfg file is valid.

        Arguments:

        """

        self.assertEqual(mysql_libs.is_cfg_valid([self.svr]), (True, []))


if __name__ == "__main__":
    unittest.main()
