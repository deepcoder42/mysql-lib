#!/usr/bin/python
# Classification (U)

"""Program:  masterrep_getloginfo.py

    Description:  Unit testing of MasterRep.get_log_info in mysql_class.py.

    Usage:
        test/unit/mysql_class/masterrep_getloginfo.py

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
import mysql_class
import lib.machine as machine
import version

__version__ = version.__version__


class UnitTest(unittest.TestCase):

    """Class:  UnitTest

    Description:  Class which is a representation of a unit testing.

    Methods:
        setUp -> Initialize testing environment.
        test_default -> Test get_log_info method.

    """

    def setUp(self):

        """Function:  setUp

        Description:  Initialization for unit testing.

        Arguments:

        """

        self.name = "Mysql_Server"
        self.server_id = 10
        self.sql_user = "mysql_user"
        self.sql_pass = "d"
        self.machine = getattr(machine, "Linux")()
        self.host = "host_server"
        self.port = 3307
        self.defaults_file = "def_cfg_file"
        self.extra_def_file = "extra_cfg_file"

    def test_default(self):

        """Function:  test_default

        Description:  Test get_log_info method.

        Arguments:

        """

        mysqlrep = mysql_class.MasterRep(self.name, self.server_id,
                                         self.sql_user, self.sql_pass,
                                         self.machine,
                                         defaults_file=self.defaults_file)

        self.assertEqual((mysqlrep.get_log_info()), (None, None))


if __name__ == "__main__":
    unittest.main()
