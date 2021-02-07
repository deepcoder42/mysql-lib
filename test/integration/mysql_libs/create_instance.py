#!/usr/bin/python
# Classification (U)

"""Program:  create_instance.py

    Description:  Integration testing of create_instance in mysql_libs.py.

    Usage:
        test/integration/mysql_libs/create_instance.py

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
        test_rep_user -> Test with passing rep_user information.
        test_create_slv_rep_inst -> Test with SlaveRep class instance.
        test_create_mst_rep_inst -> Test with MasterRep class instance.
        test_create_rep_inst -> Test with Rep class instance.
        test_create_server_inst -> Test with Server class instance.

    """

    def setUp(self):

        """Function:  setUp

        Description:  Initialization for unit testing.

        Arguments:

        """

        self.base_dir = "test/integration"
        self.config_dir = os.path.join(self.base_dir, "config")
        self.config_name = "mysql_cfg"
        self.rep_user = "REP_USER"

    def test_rep_user(self):

        """Function:  test_rep_user

        Description:  Test with passing rep_user information.

        Arguments:

        """

        srv = mysql_libs.create_instance(
            self.config_name, self.config_dir, mysql_class.SlaveRep)

        self.assertEqual(srv.rep_user, self.rep_user)

    def test_create_slv_rep_inst(self):

        """Function:  test_create_slv_rep_inst

        Description:  Test with SlaveRep class instance.

        Arguments:

        """

        srv = mysql_libs.create_instance(
            self.config_name, self.config_dir, mysql_class.SlaveRep)

        self.assertTrue(isinstance(srv, mysql_class.SlaveRep))

    def test_create_mst_rep_inst(self):

        """Function:  test_create_mst_rep_inst

        Description:  Test with MasterRep class instance.

        Arguments:

        """

        srv = mysql_libs.create_instance(
            self.config_name, self.config_dir, mysql_class.MasterRep)

        self.assertTrue(isinstance(srv, mysql_class.MasterRep))

    def test_create_rep_inst(self):

        """Function:  test_create_rep_inst

        Description:  Test with Rep class instance.

        Arguments:

        """

        srv = mysql_libs.create_instance(
            self.config_name, self.config_dir, mysql_class.Rep)

        self.assertTrue(isinstance(srv, mysql_class.Rep))

    def test_create_server_inst(self):

        """Function:  test_create_server_inst

        Description:  Test with Server class instance.

        Arguments:

        """

        srv = mysql_libs.create_instance(
            self.config_name, self.config_dir, mysql_class.Server)

        self.assertTrue(isinstance(srv, mysql_class.Server))


if __name__ == "__main__":
    unittest.main()
