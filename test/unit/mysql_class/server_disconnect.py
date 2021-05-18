#!/usr/bin/python
# Classification (U)

"""Program:  server_disconnect.py

    Description:  Unit testing of Server.disconnect in mysql_class.py.

    Usage:
        test/unit/mysql_class/server_disconnect.py

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


class Server(object):

    """Class:  Server

    Description:  Class stub holder for Server class.

    Methods:
        __init__ -> Initialize environment.
        disconnect -> Test of disconnect method.

    """

    def __init__(self):

        """Function:  __init__

        Description:  Initialize environment.

        Arguments:

        """

        pass

    def disconnect(self):

        """Function:  disconnect

        Description:  Test of disconnect method.

        Arguments:

        """

        pass


class UnitTest(unittest.TestCase):

    """Class:  UnitTest

    Description:  Class which is a representation of a unit testing.

    Methods:
        setUp -> Initialize testing environment.
        test_disconnect -> Test disconnect method.

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

        self.conn = Server()

    def test_disconnect(self):

        """Function:  test_disconnect

        Description:  Test disconnect method.

        Arguments:

        """

        mysqldb = mysql_class.Server(self.name, self.server_id, self.sql_user,
                                     self.sql_pass, self.machine,
                                     defaults_file=self.defaults_file)

        mysqldb.conn = self.conn

        self.assertFalse(mysqldb.disconnect())


if __name__ == "__main__":
    unittest.main()
