#!/usr/bin/python
# Classification (U)

"""Program:  rep_init.py

    Description:  Unit testing of Rep.__init__ in mysql_class.py.

    Usage:
        test/unit/mysql_class/rep_init.py

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
        test_no_extra_def_file -> Test with no extra_def_file arg.
        test_extra_def_file -> Test with passing extra_def_file arg.
        test_port -> Test with passing port arg.
        test_host -> Test with host arg.
        test_no_default -> Test with no default file.
        test_config -> Test with config attribute.
        test_default -> Test with minimum number of arguments.

    """

    def setUp(self):

        """Function:  setUp

        Description:  Initialization for unit testing.

        Arguments:

        """

        key1 = "pass"
        key2 = "wd"
        self.name = "Mysql_Server"
        self.server_id = 10
        self.sql_user = "mysql_user"
        self.sql_pass = "my_japd"
        self.machine = getattr(machine, "Linux")()
        self.host = "host_server"
        self.port = 3307
        self.defaults_file = "def_cfg_file"
        self.extra_def_file = "extra_cfg_file"
        self.config = {key1 + key2: self.sql_pass}

    def test_no_extra_def_file(self):

        """Function:  test_no_extra_def_file

        Description:  Test with no extra_def_file arg.

        Arguments:

        """

        mysqlrep = mysql_class.Rep(
            self.name, self.server_id, self.sql_user, self.sql_pass,
            os_type=self.machine)

        self.assertEqual(
            (mysqlrep.name, mysqlrep.server_id, mysqlrep.sql_user,
             mysqlrep.sql_pass, mysqlrep.machine, mysqlrep.host,
             mysqlrep.port, mysqlrep.extra_def_file),
            (self.name, self.server_id, self.sql_user, self.sql_pass,
             self.machine, "localhost", 3306, None))

    def test_extra_def_file(self):

        """Function:  test_extra_def_file

        Description:  Test with passing extra_def_file arg.

        Arguments:

        """

        mysqlrep = mysql_class.Rep(
            self.name, self.server_id, self.sql_user, self.sql_pass,
            os_type=self.machine, extra_def_file=self.extra_def_file)

        self.assertEqual(
            (mysqlrep.name, mysqlrep.server_id, mysqlrep.sql_user,
             mysqlrep.sql_pass, mysqlrep.machine, mysqlrep.host,
             mysqlrep.port, mysqlrep.extra_def_file),
            (self.name, self.server_id, self.sql_user, self.sql_pass,
             self.machine, "localhost", 3306, self.extra_def_file))

    def test_port(self):

        """Function:  test_port

        Description:  Test with passing port arg.

        Arguments:

        """

        mysqlrep = mysql_class.Rep(
            self.name, self.server_id, self.sql_user, self.sql_pass,
            os_type=self.machine, port=self.port)

        self.assertEqual(
            (mysqlrep.name, mysqlrep.server_id, mysqlrep.sql_user,
             mysqlrep.sql_pass, mysqlrep.machine, mysqlrep.host,
             mysqlrep.port),
            (self.name, self.server_id, self.sql_user, self.sql_pass,
             self.machine, "localhost", self.port))

    def test_host(self):

        """Function:  test_host

        Description:  Test with host arg.

        Arguments:

        """

        mysqlrep = mysql_class.Rep(
            self.name, self.server_id, self.sql_user, self.sql_pass,
            os_type=self.machine, host=self.host)

        self.assertEqual(
            (mysqlrep.name, mysqlrep.server_id, mysqlrep.sql_user,
             mysqlrep.sql_pass, mysqlrep.machine, mysqlrep.host,
             mysqlrep.port),
            (self.name, self.server_id, self.sql_user, self.sql_pass,
             self.machine, self.host, 3306))

    def test_no_default(self):

        """Function:  test_no_default

        Description:  Test with no default file.

        Arguments:

        """

        mysqlrep = mysql_class.Rep(
            self.name, self.server_id, self.sql_user, self.sql_pass,
            os_type=self.machine)

        self.assertEqual(
            (mysqlrep.name, mysqlrep.server_id, mysqlrep.sql_user,
             mysqlrep.sql_pass, mysqlrep.machine, mysqlrep.host,
             mysqlrep.port, mysqlrep.defaults_file),
            (self.name, self.server_id, self.sql_user, self.sql_pass,
             self.machine, "localhost", 3306, self.machine.defaults_file))

    def test_config(self):

        """Function:  test_config

        Description:  Test with config attribute.

        Arguments:

        """

        mysqlrep = mysql_class.Rep(
            self.name, self.server_id, self.sql_user, self.sql_pass,
            os_type=self.machine)

        self.assertEqual(
            (mysqlrep.name, mysqlrep.server_id, mysqlrep.sql_user,
             mysqlrep.sql_pass, mysqlrep.machine, mysqlrep.host,
             mysqlrep.port, mysqlrep.config),
            (self.name, self.server_id, self.sql_user, self.sql_pass,
             self.machine, "localhost", 3306, self.config))

    def test_default(self):

        """Function:  test_default

        Description:  Test __init__ method with default arguments.

        Arguments:

        """

        mysqlrep = mysql_class.Rep(
            self.name, self.server_id, self.sql_user, self.sql_pass,
            os_type=self.machine, defaults_file=self.defaults_file)

        self.assertEqual(
            (mysqlrep.name, mysqlrep.server_id, mysqlrep.sql_user,
             mysqlrep.sql_pass, mysqlrep.machine, mysqlrep.host,
             mysqlrep.port),
            (self.name, self.server_id, self.sql_user, self.sql_pass,
             self.machine, "localhost", 3306))


if __name__ == "__main__":
    unittest.main()
