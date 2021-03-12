#!/usr/bin/python
# Classification (U)

"""Program:  rep_init.py

    Description:  Integration testing of Rep.__init__ in mysql_class.py.

    Usage:
        test/integration/mysql_class/rep_init.py

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
        test_conn -> Test with conn attribute.
        test_config -> Test with config attribute.
        test_no_extra_def_file -> Test with no extra_def_file arg.
        test_extra_def_file -> Test with passing extra_def_file arg.
        test_no_port -> Test with no port arg.
        test_port -> Test with passing port arg.
        test_no_host -> Test with no host arg.
        test_host -> Test with passing host arg.
        test_no_default -> Test with no default file.
        test_default -> Test with default file.

    """

    def setUp(self):

        """Function:  setUp

        Description:  Initialization for unit testing.

        Arguments:

        """

        self.base_dir = "test/integration"
        self.config_dir = os.path.join(self.base_dir, "config")
        self.config_name = "master_mysql_cfg"
        self.cfg = gen_libs.load_module(self.config_name, self.config_dir)
        key1 = "pass"
        key2 = "wd"
        self.machine = getattr(machine, "Linux")()
        self.results = self.machine.defaults_file
        self.config = {key1 + key2: self.cfg.japd}

    def test_conn(self):

        """Function:  test_conn

        Description:  Test with conn attribute.

        Arguments:

        """

        mysqldb = mysql_class.Rep(
            self.cfg.name, self.cfg.sid, self.cfg.user, self.cfg.japd,
            os_type=getattr(machine, self.cfg.serv_os)(), host=self.cfg.host)

        self.assertEqual(mysqldb.conn, None)

    def test_config(self):

        """Function:  test_config

        Description:  Test with config attribute.

        Arguments:

        """

        mysqldb = mysql_class.Rep(
            self.cfg.name, self.cfg.sid, self.cfg.user, self.cfg.japd,
            os_type=getattr(machine, self.cfg.serv_os)(), host=self.cfg.host,
            port=self.cfg.port)

        self.assertEqual(
            (mysqldb.name, mysqldb.server_id, mysqldb.sql_user, mysqldb.host,
             mysqldb.config),
            (self.cfg.name, self.cfg.sid, self.cfg.user, self.cfg.host,
             self.config))

    def test_no_extra_def_file(self):

        """Function:  test_no_extra_def_file

        Description:  Test with no extra_def_file arg.

        Arguments:

        """

        mysqldb = mysql_class.Rep(
            self.cfg.name, self.cfg.sid, self.cfg.user, self.cfg.japd,
            os_type=getattr(machine, self.cfg.serv_os)(), host=self.cfg.host,
            port=self.cfg.port)

        self.assertEqual(mysqldb.extra_def_file, None)

    def test_extra_def_file(self):

        """Function:  test_extra_def_file

        Description:  Test with passing extra_def_file arg.

        Arguments:

        """

        mysqldb = mysql_class.Rep(
            self.cfg.name, self.cfg.sid, self.cfg.user, self.cfg.japd,
            os_type=getattr(machine, self.cfg.serv_os)(), host=self.cfg.host,
            port=self.cfg.port, extra_def_file=self.cfg.extra_def_file)

        self.assertEqual(
            (mysqldb.name, mysqldb.server_id, mysqldb.sql_user, mysqldb.host,
             mysqldb.extra_def_file),
            (self.cfg.name, self.cfg.sid, self.cfg.user, self.cfg.host,
             self.cfg.extra_def_file))

    def test_no_port(self):

        """Function:  test_no_port

        Description:  Test with no port arg.

        Arguments:

        """

        mysqldb = mysql_class.Rep(
            self.cfg.name, self.cfg.sid, self.cfg.user, self.cfg.japd,
            os_type=getattr(machine, self.cfg.serv_os)(), host=self.cfg.host)

        self.assertEqual(mysqldb.port, 3306)

    def test_port(self):

        """Function:  test_port

        Description:  Test with passing port arg.

        Arguments:

        """

        mysqldb = mysql_class.Rep(
            self.cfg.name, self.cfg.sid, self.cfg.user, self.cfg.japd,
            os_type=getattr(machine, self.cfg.serv_os)(), host=self.cfg.host,
            port=self.cfg.port)

        self.assertEqual(
            (mysqldb.name, mysqldb.server_id, mysqldb.sql_user, mysqldb.host,
             mysqldb.port),
            (self.cfg.name, self.cfg.sid, self.cfg.user, self.cfg.host,
             self.cfg.port))

    def test_no_host(self):

        """Function:  test_no_host

        Description:  Test with no host arg.

        Arguments:

        """

        mysqldb = mysql_class.Rep(
            self.cfg.name, self.cfg.sid, self.cfg.user, self.cfg.japd,
            os_type=getattr(machine, self.cfg.serv_os)(), port=self.cfg.port)

        self.assertEqual(mysqldb.host, "localhost")

    def test_host(self):

        """Function:  test_host

        Description:  Test with passing host arg.

        Arguments:

        """

        mysqldb = mysql_class.Rep(
            self.cfg.name, self.cfg.sid, self.cfg.user, self.cfg.japd,
            os_type=getattr(machine, self.cfg.serv_os)(), host=self.cfg.host,
            port=self.cfg.port)

        self.assertEqual(
            (mysqldb.name, mysqldb.server_id, mysqldb.sql_user, mysqldb.host,
             mysqldb.port),
            (self.cfg.name, self.cfg.sid, self.cfg.user, self.cfg.host,
             self.cfg.port))

    def test_no_default(self):

        """Function:  test_no_default

        Description:  Test with no default file.

        Arguments:

        """

        mysqldb = mysql_class.Rep(
            self.cfg.name, self.cfg.sid, self.cfg.user, self.cfg.japd,
            os_type=getattr(machine, self.cfg.serv_os)(), host=self.cfg.host,
            port=self.cfg.port)

        self.assertEqual(mysqldb.defaults_file, self.results)

    def test_default(self):

        """Function:  test_default

        Description:  Test with default file.

        Arguments:

        """

        mysqldb = mysql_class.Rep(
            self.cfg.name, self.cfg.sid, self.cfg.user, self.cfg.japd,
            os_type=getattr(machine, self.cfg.serv_os)(), host=self.cfg.host,
            port=self.cfg.port, defaults_file=self.cfg.cfg_file)

        self.assertEqual(
            (mysqldb.name, mysqldb.server_id, mysqldb.sql_user, mysqldb.host,
             mysqldb.port, mysqldb.defaults_file),
            (self.cfg.name, self.cfg.sid, self.cfg.user, self.cfg.host,
             self.cfg.port, self.cfg.cfg_file))


if __name__ == "__main__":
    unittest.main()
