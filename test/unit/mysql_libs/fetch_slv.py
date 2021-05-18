#!/usr/bin/python
# Classification (U)

"""Program:  fetch_slv.py

    Description:  Unit testing of fetch_slv in mysql_libs.py.

    Usage:
        test/unit/mysql_libs/fetch_slv.py

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

    def __init__(self, name):

        """Method:  __init__

        Description:  Class initialization.

        Arguments:

        """

        self.name = name


class UnitTest(unittest.TestCase):

    """Class:  UnitTest

    Description:  Class which is a representation of a unit testing.

    Methods:
        setUp -> Initialize testing environment.
        test_slave_not_found -> Test with slave not found.
        test_slave_found -> Test with slave found.

    """

    def setUp(self):

        """Function:  setUp

        Description:  Initialization for unit testing.

        Arguments:

        """

        self.slave1 = Server("Slave1")
        self.slave2 = Server("Slave2")
        self.slv_list = []
        self.slv_list.append(self.slave1)
        self.slv_list.append(self.slave2)
        self.slave = "Slave3"
        self.err_msg = \
            "Error:  Slave %s was not found in slave array." % (self.slave)

    @mock.patch("mysql_libs.find_name")
    def test_slave_not_found(self, mock_find):

        """Function:  test_slave_not_found

        Description:  Test with slave not found.

        Arguments:

        """

        mock_find.return_value = None

        self.assertEqual(mysql_libs.fetch_slv(self.slv_list, self.slave),
                         (None, True, self.err_msg))

    @mock.patch("mysql_libs.find_name")
    def test_slave_found(self, mock_find):

        """Function:  test_slave_found

        Description:  Test with slave found.

        Arguments:

        """

        mock_find.return_value = "Slave1"
        _, err_flag, err_msg = mysql_libs.fetch_slv(self.slv_list, "Slave1")

        self.assertEqual((err_flag, err_msg), (False, None))


if __name__ == "__main__":
    unittest.main()
