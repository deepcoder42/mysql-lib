#!/usr/bin/python
# Classification (U)

"""Program:  create_slv_array.py

    Description:  Integration testing of create_slv_array in mysql_libs.py.

    Usage:
        test/integration/mysql_libs/create_slv_array.py

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
import lib.cmds_gen as cmds_gen
import version

__version__ = version.__version__


class UnitTest(unittest.TestCase):

    """Class:  UnitTest

    Description:  Class which is a representation of a unit testing.

    Methods:
        setUp -> Initialize testing environment.
        test_create_slv_array2 -> Test create_slv_array function.
        test_create_slv_array -> Test create_slv_array function.

    """

    def setUp(self):

        """Function:  setUp

        Description:  Initialization for unit testing.

        Arguments:

        """

        self.base_dir = "test/integration"
        self.config_dir = os.path.join(self.base_dir, "config")
        self.config_name = "slave.txt"

    def test_create_slv_array2(self):

        """Function:  test_create_slv_array2

        Description:  Test create_slv_array function.

        Arguments:

        """

        slaves = cmds_gen.create_cfg_array(self.config_name,
                                           cfg_path=self.config_dir)
        srv = mysql_libs.create_slv_array(slaves)

        self.assertTrue(isinstance(srv[0], mysql_class.SlaveRep))

    def test_create_slv_array(self):

        """Function:  test_create_slv_array

        Description:  Test create_slv_array function.

        Arguments:

        """

        slaves = cmds_gen.create_cfg_array(self.config_name,
                                           cfg_path=self.config_dir)
        srv = mysql_libs.create_slv_array(slaves)

        self.assertTrue(isinstance(srv, list))


if __name__ == "__main__":
    unittest.main()
