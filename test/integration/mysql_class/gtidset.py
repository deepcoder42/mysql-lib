#!/usr/bin/python
# Classification (U)

"""Program:  gtidset.py

    Description:  Integration testing of GTIDSet class in mysql_class.py.

    Usage:
        test/integration/mysql_class/gtidset.py

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
        test_greater_than -> Test with GTIDSets greater than.
        test_less_than -> Test with GTIDSets less than.
        test_not_equal -> Test with GTIDSets not equal.
        test_greater_than_equal -> Test with GTIDSets greater than equal.
        test_less_than_equal -> Test with GTIDSets less than equal.
        test_equal -> Test with GTIDSets equal.
        test_string2 -> Test conversion of GTIDSet to string.
        test_string -> Test conversion of GTIDSet to string.
        test_is_class -> Test is GTIDSets class.

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
        self.svr2 = mysql_class.SlaveRep(
            self.cfg.name, self.cfg.sid, self.cfg.user, self.cfg.japd,
            os_type=getattr(machine, self.cfg.serv_os)(), host=self.cfg.host,
            port=self.cfg.port, defaults_file=self.cfg.cfg_file)
        self.svr2.connect()

    def test_greater_than(self):

        """Function:  test_greater_than

        Description:  Test with GTIDSets greater than.

        Arguments:

        """

        self.assertFalse(self.svr.exe_gtidset > self.svr2.exe_gtidset)

    def test_less_than(self):

        """Function:  test_less_than

        Description:  Test with GTIDSets less than.

        Arguments:

        """

        self.assertFalse(self.svr.exe_gtidset < self.svr2.exe_gtidset)

    def test_not_equal(self):

        """Function:  test_not_equal

        Description:  Test with GTIDSets not equal.

        Arguments:

        """

        self.assertFalse(self.svr.exe_gtidset != self.svr2.exe_gtidset)

    def test_greater_than_equal(self):

        """Function:  test_greater_than_equal

        Description:  Test with GTIDSets greater than equal.

        Arguments:

        """

        self.assertTrue(self.svr.exe_gtidset >= self.svr2.exe_gtidset)

    def test_less_than_equal(self):

        """Function:  test_less_than_equal

        Description:  Test with GTIDSets less than equal.

        Arguments:

        """

        self.assertTrue(self.svr.exe_gtidset <= self.svr2.exe_gtidset)

    def test_equal(self):

        """Function:  test_equal

        Description:  Test with GTIDSets equal.

        Arguments:

        """

        self.assertTrue(self.svr.exe_gtidset == self.svr2.exe_gtidset)

    def test_string2(self):

        """Function:  test_string2

        Description:  Test conversion of GTIDSet to string.

        Arguments:

        """

        line = "%s" % self.svr.exe_gtidset

        self.assertTrue(isinstance(line, str))

    def test_string(self):

        """Function:  test_string

        Description:  Test conversion of GTIDSet to string.

        Arguments:

        """

        line = str(self.svr.exe_gtidset)

        self.assertTrue(isinstance(line, str))

    def test_is_class(self):

        """Function:  test_is_class

        Description:  Test is GTIDSets class.

        Arguments:

        """

        self.assertTrue(isinstance(self.svr.exe_gtidset, mysql_class.GTIDSet))


if __name__ == "__main__":
    unittest.main()
