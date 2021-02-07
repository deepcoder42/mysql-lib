#!/usr/bin/python
# Classification (U)

"""Program:  crt_srv_inst.py

    Description:  Integration testing of crt_srv_inst in mysql_libs.py.

    Usage:
        test/integration/mysql_libs/crt_srv_inst.py

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
        test_crt_srv_inst -> Test crt_srv_inst function.

    """

    def setUp(self):

        """Function:  setUp

        Description:  Initialization for unit testing.

        Arguments:

        """

        self.base_dir = "test/integration"
        self.config_dir = os.path.join(self.base_dir, "config")
        self.config_name = "mysql_cfg"

    def test_crt_srv_inst(self):

        """Function:  test_crt_srv_inst

        Description:  Test crt_srv_inst function.

        Arguments:

        """

        srv = mysql_libs.crt_srv_inst(self.config_name, self.config_dir)

        self.assertTrue(isinstance(srv, mysql_class.Server))


if __name__ == "__main__":
    unittest.main()
