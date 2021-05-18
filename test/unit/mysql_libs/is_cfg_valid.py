#!/usr/bin/python
# Classification (U)

"""Program:  is_cfg_valid.py

    Description:  Unit testing of is_cfg_valid in mysql_libs.py.

    Usage:
        test/unit/mysql_libs/is_cfg_valid.py

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
import mock

# Local
sys.path.append(os.getcwd())
import mysql_libs
import version

__version__ = version.__version__


class Server(object):

    """Class:  Server

    Description:  Class stub holder for Server class.

    Methods:
        __init__ -> Class initialization.

    """

    def __init__(self, name, def_file=None):

        """Method:  __init__

        Description:  Class initialization.

        Arguments:

        """

        self.name = name
        self.extra_def_file = def_file


class UnitTest(unittest.TestCase):

    """Class:  UnitTest

    Description:  Class which is a representation of a unit testing.

    Methods:
        setUp -> Initialize testing environment.
        test_multi_both_fail -> Test with multiple servers with both failed.
        test_multi_one_fail -> Test with multiple servers with one failed.
        test_multi_servers -> Test with multiple servers valid.
        test_no_extra_file -> Test with no extra file present.
        test_chk_fails -> Test with check file fails.
        test_cfg_valid -> Test with extra cfg file is valid.

    """

    def setUp(self):

        """Function:  setUp

        Description:  Initialization for unit testing.

        Arguments:

        """

        msg = "Error Message"
        self.slave1 = Server("Slave1", "Extra_Def_File")
        self.slave2 = Server("Slave2")
        self.err_msg = msg
        self.err_msg2 = [msg, "Slave1:  Extra_Def_File is missing."]
        self.results = ["Slave2:  extra_def_file is not set."]
        self.results2 = [msg, "Slave1:  Extra_Def_File is missing.",
                         "Slave2:  extra_def_file is not set."]

    @mock.patch("mysql_libs.gen_libs.chk_crt_file")
    def test_multi_both_fail(self, mock_chk):

        """Function:  test_multi_both_fail

        Description:  Test with multiple servers with both failed.

        Arguments:

        """

        mock_chk.return_value = (False, self.err_msg)

        self.assertEqual(mysql_libs.is_cfg_valid([self.slave1, self.slave2]),
                         (False, self.results2))

    @mock.patch("mysql_libs.gen_libs.chk_crt_file")
    def test_multi_one_fail(self, mock_chk):

        """Function:  test_multi_one_fail

        Description:  Test with multiple servers with one failed.

        Arguments:

        """

        mock_chk.return_value = (True, None)

        self.assertEqual(mysql_libs.is_cfg_valid([self.slave1, self.slave2]),
                         (False, self.results))

    @mock.patch("mysql_libs.gen_libs.chk_crt_file")
    def test_multi_servers(self, mock_chk):

        """Function:  test_multi_servers

        Description:  Test with multiple servers valid.

        Arguments:

        """

        mock_chk.return_value = (True, None)

        self.assertEqual(mysql_libs.is_cfg_valid([self.slave1, self.slave1]),
                         (True, []))

    def test_no_extra_file(self):

        """Function:  test_no_extra_file

        Description:  Test with no extra file present.

        Arguments:

        """

        self.assertEqual(mysql_libs.is_cfg_valid([self.slave2]),
                         (False, self.results))

    @mock.patch("mysql_libs.gen_libs.chk_crt_file")
    def test_chk_fails(self, mock_chk):

        """Function:  test_chk_fails

        Description:  Test with check file fails.

        Arguments:

        """

        mock_chk.return_value = (False, self.err_msg)

        self.assertEqual(mysql_libs.is_cfg_valid([self.slave1]),
                         (False, self.err_msg2))

    @mock.patch("mysql_libs.gen_libs.chk_crt_file")
    def test_cfg_valid(self, mock_chk):

        """Function:  test_cfg_valid

        Description:  Test with extra cfg file is valid.

        Arguments:

        """

        mock_chk.return_value = (True, None)

        self.assertEqual(mysql_libs.is_cfg_valid([self.slave1]), (True, []))


if __name__ == "__main__":
    unittest.main()
