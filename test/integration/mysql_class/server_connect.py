#!/usr/bin/python
# Classification (U)

"""Program:  server_connect.py

    Description:  Integration testing of Server.connect in mysql_class.py.

    Usage:
        test/integration/mysql_class/server_connect.py

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
import lib.gen_libs as gen_libs
import lib.machine as machine
import version

__version__ = version.__version__


class UnitTest(unittest.TestCase):

    """Class:  UnitTest

    Description:  Class which is a representation of a unit testing.

    Methods:
        setUp -> Initialize testing environment.
        test_silent -> Test silent option.
        test_conn_msg2 -> Test conn_msg attribute failed connection.
        test_conn_msg -> Test conn_msg attribute failed connection.
        test_database -> Test with database argument passed.
        test_config -> Test with config attribute.
        test_connect_exception -> Test connection method exception.
        test_connect -> Test connect method.

    """

    def setUp(self):

        """Function:  setUp

        Description:  Initialization for unit testing.

        Arguments:

        """

        self.base_dir = "test/integration"
        self.config_dir = os.path.join(self.base_dir, "config")
        self.config_name = "mysql_cfg"
        self.cfg = gen_libs.load_module(self.config_name, self.config_dir)
        self.svr = mysql_class.Server(
            self.cfg.name, self.cfg.sid, self.cfg.user, self.cfg.japd,
            os_type=getattr(machine, self.cfg.serv_os)(), host=self.cfg.host,
            port=self.cfg.port, defaults_file=self.cfg.cfg_file)
        self.database = "mysql"
        self.results = "Couldn't connect to database.  MySQL error 1045:"

    def test_silent(self):

        """Function:  test_silent

        Description:  Test silent option.

        Arguments:

        """

        svr = mysql_class.Server(
            self.cfg.name, self.cfg.sid, self.cfg.user, "testme",
            os_type=getattr(machine, self.cfg.serv_os)(), host=self.cfg.host,
            port=self.cfg.port, defaults_file=self.cfg.cfg_file)

        svr.connect(silent=True)

        self.assertEqual(svr.conn_msg[:48], self.results)

    def test_conn_msg2(self):

        """Function:  test_conn_msg2

        Description:  Test conn_msg attribute successful connection.

        Arguments:

        """

        self.svr.connect()

        self.assertFalse(self.svr.conn_msg)

    def test_conn_msg(self):

        """Function:  test_conn_msg

        Description:  Test conn_msg attribute failed connection.

        Arguments:

        """

        svr = mysql_class.Server(
            self.cfg.name, self.cfg.sid, self.cfg.user, "testme",
            os_type=getattr(machine, self.cfg.serv_os)(), host=self.cfg.host,
            port=self.cfg.port, defaults_file=self.cfg.cfg_file)

        with gen_libs.no_std_out():
            svr.connect()

        self.assertEqual(svr.conn_msg[:48], self.results)

    def test_database(self):

        """Function:  test_database

        Description:  Test with database argument passed.

        Arguments:

        """

        self.svr.connect(database=self.database)

        self.assertEqual(self.svr.conn.database, self.database)

    def test_config(self):

        """Function:  test_config

        Description:  Test with config attribute.

        Arguments:

        """

        self.svr.connect()

        self.assertTrue(self.svr.config)

    def test_connect_exception(self):

        """Function:  test_connect_exception

        Description:  Test connection method exception.

        Arguments:

        """

        svr = mysql_class.Server(
            self.cfg.name, self.cfg.sid, self.cfg.user, "testme",
            os_type=getattr(machine, self.cfg.serv_os)(), host=self.cfg.host,
            port=self.cfg.port, defaults_file=self.cfg.cfg_file)

        with gen_libs.no_std_out():
            svr.connect()

        self.assertFalse(svr.conn)

    def test_connect(self):

        """Function:  test_connect

        Description:  Test connect method.

        Arguments:

        """

        self.svr.connect()

        self.assertTrue(self.svr.conn)


if __name__ == "__main__":
    unittest.main()
