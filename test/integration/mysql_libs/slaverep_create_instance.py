#!/usr/bin/python
# Classification (U)

"""Program:  slaverep_create_instance.py

    Description:  Integration testing of create_instance in mysql_libs.py.

    Usage:
        test/integration/mysql_libs/slaverep_create_instance.py

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
import version

__version__ = version.__version__


class UnitTest(unittest.TestCase):

    """Class:  UnitTest

    Description:  Class which is a representation of a unit testing.

    Methods:
        setUp -> Initialize testing environment.
        test_create_instance -> Test create_instance function.

    """

    def setUp(self):

        """Function:  setUp

        Description:  Initialization for unit testing.

        Arguments:

        """

        self.base_dir = "test/integration"
        self.config_dir = os.path.join(self.base_dir, "config")
        self.config_name = "slave_mysql_cfg"

    def test_create_instance(self):

        """Function:  test_create_instance

        Description:  Test create_instance function.

        Arguments:

        """

        srv = mysql_libs.create_instance(
            self.config_name, self.config_dir, mysql_class.SlaveRep)

        self.assertTrue(isinstance(srv, mysql_class.SlaveRep))


if __name__ == "__main__":
    unittest.main()
