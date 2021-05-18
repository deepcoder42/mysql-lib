#!/usr/bin/python
# Classification (U)

"""Program:  wait_until.py

    Description:  Unit testing of wait_until in mysql_libs.py.

    Usage:
        test/unit/mysql_libs/wait_until.py

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
import lib.gen_libs as gen_libs
import mysql_libs
import version

__version__ = version.__version__


class SlaveRep(object):

    """Class:  SlaveRep

    Description:  Class stub holder for mysql_class.SlaveRep class.

    Methods:
        __init__ -> Class initialization.

    """

    def __init__(self, gtid_mode="Yes"):

        """Method:  __init__

        Description:  Class initialization.

        Arguments:

        """

        self.gtid_mode = gtid_mode
        self.name = "Slave"
        self.retrieved_gtid = 10
        self.mst_log = "mst_log"
        self.mst_read_pos = 12345
        self.exe_gtid = 12345
        self.relay_mst_log = "relay_mst_log"
        self.exec_mst_pos = 12345

    def upd_slv_status(self):

        """Method:  upd_slv_status

        Description:  Stub holder for mysql_class.Server.upd_slv_status method.

        Arguments:

        """

        return True


class UnitTest(unittest.TestCase):

    """Class:  UnitTest

    Description:  Class which is a representation of a unit testing.

    Methods:
        setUp -> Initialize testing environment.
        test_sql_non_gtid_good -> Test in SQL in non-GTID Mode w/ good status.
        test_sql_gtid_good -> Test in SQL in GTID Mode with good status.
        test_io_non_gtid_good -> Test in IO in non-GTID Mode with good status.
        test_io_gtid_good -> Test in IO in GTID Mode with good status.

    """

    def setUp(self):

        """Function:  setUp

        Description:  Initialization for unit testing.

        Arguments:

        """

        self.slave = SlaveRep()

    def test_sql_non_gtid_good(self):

        """Function:  test_sql_non_gtid_good

        Description:  Test in SQL in non-GTID Mode with good status.

        Arguments:

        """

        self.slave.gtid_mode = None

        with gen_libs.no_std_out():
            self.assertFalse(mysql_libs.wait_until(self.slave, "SQL",
                                                   log_file="relay_mst_log",
                                                   log_pos=12345, gtid=12345))

    def test_sql_gtid_good(self):

        """Function:  test_sql_gtid_good

        Description:  Test in SQL in GTID Mode with good status.

        Arguments:

        """

        with gen_libs.no_std_out():
            self.assertFalse(mysql_libs.wait_until(self.slave, "SQL",
                                                   gtid=12345))

    def test_io_non_gtid_good(self):

        """Function:  test_io_non_gtid_good

        Description:  Test in IO in non-GTID Mode with good status.

        Arguments:

        """

        self.slave.gtid_mode = None

        with gen_libs.no_std_out():
            self.assertFalse(mysql_libs.wait_until(self.slave, "IO",
                                                   log_file="mst_log",
                                                   log_pos=12345, gtid=10))

    def test_io_gtid_good(self):

        """Function:  test_io_gtid_good

        Description:  Test in IO in GTID Mode with good status.

        Arguments:

        """

        with gen_libs.no_std_out():
            self.assertFalse(mysql_libs.wait_until(self.slave, "IO", gtid=10))


if __name__ == "__main__":
    unittest.main()
