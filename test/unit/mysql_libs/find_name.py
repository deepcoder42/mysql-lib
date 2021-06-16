#!/usr/bin/python
# Classification (U)

"""Program:  find_name.py

    Description:  Unit testing of find_name in mysql_libs.py.

    Usage:
        test/unit/mysql_libs/find_name.py

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

    def test_slave_not_found(self):

        """Function:  test_slave_not_found

        Description:  Test with slave not found.

        Arguments:

        """

        self.assertEqual(mysql_libs.find_name(self.slv_list, "Slave3"), None)

    def test_slave_found(self):

        """Function:  test_slave_found

        Description:  Test with slave found.

        Arguments:

        """

        self.assertEqual(mysql_libs.find_name(self.slv_list, "Slave1"),
                         self.slave1)


if __name__ == "__main__":
    unittest.main()
