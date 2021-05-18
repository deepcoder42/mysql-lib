#!/usr/bin/python
# Classification (U)

"""Program:  find_name.py

    Description:  Integration testing of find_name in mysql_libs.py.

    Usage:
        test/integration/mysql_libs/find_name.py

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
        test_not_found -> Test with slave not found.
        test_found -> Test with slave found.

    """

    def setUp(self):

        """Function:  setUp

        Description:  Initialization for unit testing.

        Arguments:

        """

        self.base_dir = "test/integration"
        self.config_dir = os.path.join(self.base_dir, "config")
        self.config_name = "slave.txt"
        self.name = "NotFoundSlave"

    def test_not_found(self):

        """Function:  test_not_found

        Description:  Test with slave not found.

        Arguments:

        """

        slaves = cmds_gen.create_cfg_array(self.config_name,
                                           cfg_path=self.config_dir)
        servers = mysql_libs.create_slv_array(slaves)
        slv = mysql_libs.find_name(servers, self.name)

        self.assertFalse(slv)

    def test_found(self):

        """Function:  test_found

        Description:  Test with slave found.

        Arguments:

        """

        slaves = cmds_gen.create_cfg_array(self.config_name,
                                           cfg_path=self.config_dir)
        name = slaves[0]["name"]
        servers = mysql_libs.create_slv_array(slaves)
        slv = mysql_libs.find_name(servers, name)

        self.assertTrue(isinstance(slv, mysql_class.SlaveRep))


if __name__ == "__main__":
    unittest.main()
