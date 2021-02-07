#!/usr/bin/python
# Classification (U)

"""Program:  is_rep_delay.py

    Description:  Unit testing of is_rep_delay in mysql_libs.py.

    Usage:
        test/unit/mysql_libs/is_rep_delay.py

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
import version

__version__ = version.__version__


class MasterRep(object):

    """Class:  MasterRep

    Description:  Class stub holder for mysql_class.MasterRep class.

    Methods:
        __init__ -> Class initialization.

    """

    def __init__(self, gtid_mode, exe_gtid, filename, pos):

        """Method:  __init__

        Description:  Class initialization.

        Arguments:

        """

        self.gtid_mode = gtid_mode
        self.exe_gtid = exe_gtid
        self.file = filename
        self.pos = pos


class SlaveRep(object):

    """Class:  SlaveRep

    Description:  Class stub holder for mysql_class.SlaveRep class.

    Methods:
        __init__ -> Class initialization.

    """

    def __init__(self, gtid_mode, ret_gtid, mst_log, mst_pos, exe_gtid,
                 **kwargs):

        """Method:  __init__

        Description:  Class initialization.

        Arguments:

        """

        self.gtid_mode = gtid_mode
        self.retrieved_gtid = ret_gtid
        self.mst_log = mst_log
        self.mst_read_pos = mst_pos
        self.exe_gtid = exe_gtid
        self.relay_mst_log = kwargs.get("relay_log")
        self.exec_mst_pos = kwargs.get("exe_pos")


class UnitTest(unittest.TestCase):

    """Class:  UnitTest

    Description:  Class which is a representation of a unit testing.

    Methods:
        setUp -> Initialize testing environment.
        test_sql_not_synced_non_gtid -> Test SQL is not synced with non-GTID.
        test_sql_synced_non_gtid -> Test with SQL is synced with non-GTID.
        test_sql_not_synced_gtid -> Test with SQL is not synced with GTID.
        test_sql_synced_gtid -> Test with SQL is synced with GTID.
        test_io_not_synced_non_gtid -> Test w/ IO is not synced with non-GTID.
        test_io_synced_non_gtid -> Test with IO is synced with non-GTID
        test_io_not_synced_gtid -> Test with IO is not synced with GTID.
        test_io_synced_gtid -> Test with IO is synced with GTID.

    """

    def setUp(self):

        """Function:  setUp

        Description:  Initialization for unit testing.

        Arguments:

        """

        pass

    def test_sql_not_synced_non_gtid(self):

        """Function:  test_sql_not_synced_non_gtid

        Description:  Test with SQL is not synced with non-GTID.

        Arguments:

        """

        master = MasterRep(None, None, "File1", 12345)
        slave = SlaveRep(None, None, None, None, None, relay_log="File1",
                         exe_pos=12346)

        self.assertTrue(mysql_libs.is_rep_delay(master, slave, "SQL"))

    def test_sql_synced_non_gtid(self):

        """Function:  test_sql_synced_non_gtid

        Description:  Test with SQL is synced with non-GTID.

        Arguments:

        """

        master = MasterRep(None, None, "File1", 12345)
        slave = SlaveRep(None, None, None, None, None, relay_log="File1",
                         exe_pos=12345)

        self.assertFalse(mysql_libs.is_rep_delay(master, slave, "SQL"))

    def test_sql_not_synced_gtid(self):

        """Function:  test_sql_not_synced_gtid

        Description:  Test with SQL is not synced with GTID.

        Arguments:

        """

        master = MasterRep("Yes", 12345, None, None)
        slave = SlaveRep("Yes", None, None, None, 12346, relay_log=None,
                         exe_pos=None)

        self.assertTrue(mysql_libs.is_rep_delay(master, slave, "SQL"))

    def test_sql_synced_gtid(self):

        """Function:  test_sql_synced_gtid

        Description:  Test with SQL is synced with GTID.

        Arguments:

        """

        master = MasterRep("Yes", 12345, None, None)
        slave = SlaveRep("Yes", None, None, None, 12345, relay_log=None,
                         exe_pos=None)

        self.assertFalse(mysql_libs.is_rep_delay(master, slave, "SQL"))

    def test_io_not_synced_non_gtid(self):

        """Function:  test_io_not_synced_non_gtid

        Description:  Test with IO is not synced with non-GTID.

        Arguments:

        """

        master = MasterRep(None, None, "File1", 12345)
        slave = SlaveRep(None, None, "File1", 12346, None, relay_log=None,
                         exe_pos=None)

        self.assertTrue(mysql_libs.is_rep_delay(master, slave, "IO"))

    def test_io_synced_non_gtid(self):

        """Function:  test_io_synced_non_gtid

        Description:  Test with IO is synced with non-GTID.

        Arguments:

        """

        master = MasterRep(None, None, "File1", 12345)
        slave = SlaveRep(None, None, "File1", 12345, None, relay_log=None,
                         exe_pos=None)

        self.assertFalse(mysql_libs.is_rep_delay(master, slave, "IO"))

    def test_io_not_synced_gtid(self):

        """Function:  test_io_not_synced_gtid

        Description:  Test with IO is not synced with GTID.

        Arguments:

        """

        master = MasterRep("Yes", 12345, None, None)
        slave = SlaveRep("Yes", 12346, None, None, None, relay_log=None,
                         exe_pos=None)

        self.assertTrue(mysql_libs.is_rep_delay(master, slave, "IO"))

    def test_io_synced_gtid(self):

        """Function:  test_io_synced_gtid

        Description:  Test with IO is synced with GTID.

        Arguments:

        """

        master = MasterRep("Yes", 12345, None, None)
        slave = SlaveRep("Yes", 12345, None, None, None, relay_log=None,
                         exe_pos=None)

        self.assertFalse(mysql_libs.is_rep_delay(master, slave, "IO"))


if __name__ == "__main__":
    unittest.main()
