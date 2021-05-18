#!/usr/bin/python
# Classification (U)

"""Program:  server_vertsql.py

    Description:  Unit testing of Server.vert_sql in mysql_class.py.

    Usage:
        test/unit/mysql_class/server_vertsql.py

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
import mysql_class
import lib.machine as machine
import version

__version__ = version.__version__


class UnitTest(unittest.TestCase):

    """Class:  UnitTest

    Description:  Class which is a representation of a unit testing.

    Methods:
        setUp -> Initialize testing environment.
        test_vert_sql -> Test vert_sql method.

    """

    def setUp(self):

        """Function:  setUp

        Description:  Initialization for unit testing.

        Arguments:

        """

        self.name = "Mysql_Server"
        self.server_id = 10
        self.sql_user = "mysql_user"
        self.sql_pass = "my_japd"
        self.machine = getattr(machine, "Linux")()
        self.host = "host_server"
        self.port = 3307
        self.defaults_file = "def_cfg_file"
        self.extra_def_file = "extra_cfg_file"

        self.data = [("Column1", "Value1"), ("Column2", "Value2")]
        self.results = {"Column1": "Value1", "Column2": "Value2"}

    @mock.patch("mysql_class.Server.sql")
    def test_vert_sql(self, mock_sql):

        """Function:  test_vert_sql

        Description:  Test vert_sql method.

        Arguments:

        """

        mock_sql.return_value = self.data
        mysqldb = mysql_class.Server(self.name, self.server_id, self.sql_user,
                                     self.sql_pass, self.machine,
                                     defaults_file=self.defaults_file)

        self.assertEqual(mysqldb.vert_sql('SQL_Query'), self.results)


if __name__ == "__main__":
    unittest.main()
