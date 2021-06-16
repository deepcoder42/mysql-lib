#!/usr/bin/python
# Classification (U)

"""Program:  server_init.py

    Description:  Unit testing of Server.__init__ in mysql_class.py.

    Usage:
        test/unit/mysql_class/server_init.py

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
import mysql.connector

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
        test_ssl_config7 -> Test config with ssl attributes set.
        test_ssl_config6 -> Test config with ssl attributes set.
        test_ssl_config5 -> Test config with ssl attributes set.
        test_ssl_config4 -> Test config with ssl attributes set.
        test_ssl_config3 -> Test config with ssl attributes set.
        test_ssl_config2 -> Test config with ssl attributes set.
        test_ssl_config -> Test config with ssl attributes set.
        test_ssl_verify_cert2 -> Test with ssl_verify_cert attribute.
        test_ssl_verify_cert -> Test with ssl_verify_cert attribute.
        test_ssl_verify_id2 -> Test with ssl_verify_id attribute.
        test_ssl_verify_id -> Test with ssl_verify_id attribute.
        test_ssl_disabled2 -> Test with ssl_disabled attribute.
        test_ssl_disabled -> Test with ssl_disabled attribute.
        test_ssl_client_flag2 -> Test with ssl_client_flag attribute.
        test_ssl_client_flag -> Test with ssl_client_flag attribute.
        test_ssl_client_cert2 -> Test with ssl_client_cert attribute.
        test_ssl_client_cert -> Test with ssl_client_cert attribute.
        test_ssl_client_key2 -> Test with ssl_client_key attribute.
        test_ssl_client_key -> Test with ssl_client_key attribute.
        test_ssl_client_ca2 -> Test with ssl_client_ca attribute.
        test_ssl_client_ca -> Test with ssl_client_ca attribute.
        test_sql_pass -> Test with sql_pass attribute.
        test_indb_buf_write -> Test with indb_buf_write attribute.
        test_version -> Test with version attribute.
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
        self.results = self.machine.defaults_file

        self.config = {}
        self.config[key1 + key2] = self.sql_pass

        self.config2 = {}
        self.config2[key1 + key2] = self.sql_pass
        self.config2["ssl_ca"] = "CAFile"
        self.config2["client_flags"] = [mysql.connector.ClientFlag.SSL]
        self.config2["ssl_disabled"] = False
        self.config2["ssl_verify_identity"] = False
        self.config2["ssl_verify_cert"] = False

        self.config3 = {}
        self.config3[key1 + key2] = self.sql_pass
        self.config3["ssl_key"] = "KeyFile"
        self.config3["ssl_cert"] = "CertFile"
        self.config3["client_flags"] = [mysql.connector.ClientFlag.SSL]
        self.config3["ssl_ca"] = ""
        self.config3["ssl_disabled"] = False
        self.config3["ssl_verify_identity"] = False

        self.config4 = {}
        self.config4[key1 + key2] = self.sql_pass
        self.config4["ssl_ca"] = "CAFile"
        self.config4["ssl_key"] = "KeyFile"
        self.config4["ssl_cert"] = "CertFile"
        self.config4["client_flags"] = [mysql.connector.ClientFlag.SSL]
        self.config4["ssl_disabled"] = False
        self.config4["ssl_verify_identity"] = False
        self.config4["ssl_verify_cert"] = False

        self.config5 = {}
        self.config5[key1 + key2] = self.sql_pass
        self.config5["ssl_ca"] = "CAFile"
        self.config5["ssl_key"] = "KeyFile"
        self.config5["ssl_cert"] = "CertFile"
        self.config5["client_flags"] = [4096]
        self.config5["ssl_disabled"] = False
        self.config5["ssl_verify_identity"] = False
        self.config5["ssl_verify_cert"] = False

        self.config6 = {}
        self.config6[key1 + key2] = self.sql_pass
        self.config6["ssl_ca"] = "CAFile"
        self.config6["ssl_key"] = "KeyFile"
        self.config6["ssl_cert"] = "CertFile"
        self.config6["client_flags"] = [4096]
        self.config6["ssl_disabled"] = True
        self.config6["ssl_verify_identity"] = False
        self.config6["ssl_verify_cert"] = False

        self.config7 = {}
        self.config7[key1 + key2] = self.sql_pass
        self.config7["ssl_ca"] = "CAFile"
        self.config7["ssl_key"] = "KeyFile"
        self.config7["ssl_cert"] = "CertFile"
        self.config7["client_flags"] = [4096]
        self.config7["ssl_disabled"] = False
        self.config7["ssl_verify_identity"] = True
        self.config7["ssl_verify_cert"] = False

        self.config8 = {}
        self.config8[key1 + key2] = self.sql_pass
        self.config8["ssl_ca"] = "CAFile"
        self.config8["ssl_key"] = "KeyFile"
        self.config8["ssl_cert"] = "CertFile"
        self.config8["client_flags"] = [4096]
        self.config8["ssl_disabled"] = False
        self.config8["ssl_verify_identity"] = False
        self.config8["ssl_verify_cert"] = True

    def test_ssl_config7(self):

        """Function:  test_ssl_config7

        Description:  Test config with ssl attributes set.

        Arguments:

        """

        mysqldb = mysql_class.Server(
            self.name, self.server_id, self.sql_user, self.sql_pass,
            os_type=self.machine, ssl_client_ca="CAFile",
            ssl_client_key="KeyFile", ssl_client_cert="CertFile",
            ssl_client_flag=4096, ssl_verify_cert=True)

        self.assertEqual(mysqldb.config, self.config8)

    def test_ssl_config6(self):

        """Function:  test_ssl_config6

        Description:  Test config with ssl attributes set.

        Arguments:

        """

        mysqldb = mysql_class.Server(
            self.name, self.server_id, self.sql_user, self.sql_pass,
            os_type=self.machine, ssl_client_ca="CAFile",
            ssl_client_key="KeyFile", ssl_client_cert="CertFile",
            ssl_client_flag=4096, ssl_verify_id=True)

        self.assertEqual(mysqldb.config, self.config7)

    def test_ssl_config5(self):

        """Function:  test_ssl_config5

        Description:  Test config with ssl attributes set.

        Arguments:

        """

        mysqldb = mysql_class.Server(
            self.name, self.server_id, self.sql_user, self.sql_pass,
            os_type=self.machine, ssl_client_ca="CAFile",
            ssl_client_key="KeyFile", ssl_client_cert="CertFile",
            ssl_client_flag=4096, ssl_disabled=True)

        self.assertEqual(mysqldb.config, self.config6)

    def test_ssl_config4(self):

        """Function:  test_ssl_config4

        Description:  Test config with ssl attributes set.

        Arguments:

        """

        mysqldb = mysql_class.Server(
            self.name, self.server_id, self.sql_user, self.sql_pass,
            os_type=self.machine, ssl_client_ca="CAFile",
            ssl_client_key="KeyFile", ssl_client_cert="CertFile",
            ssl_client_flag=4096)

        self.assertEqual(mysqldb.config, self.config5)

    def test_ssl_config3(self):

        """Function:  test_ssl_config3

        Description:  Test config with ssl attributes set.

        Arguments:

        """

        mysqldb = mysql_class.Server(
            self.name, self.server_id, self.sql_user, self.sql_pass,
            os_type=self.machine, ssl_client_ca="CAFile",
            ssl_client_key="KeyFile", ssl_client_cert="CertFile")

        self.assertEqual(mysqldb.config, self.config4)

    def test_ssl_config2(self):

        """Function:  test_ssl_config2

        Description:  Test config with ssl attributes set.

        Arguments:

        """

        mysqldb = mysql_class.Server(
            self.name, self.server_id, self.sql_user, self.sql_pass,
            os_type=self.machine, ssl_client_key="KeyFile",
            ssl_client_cert="CertFile")

        self.assertEqual(mysqldb.config, self.config3)

    def test_ssl_config(self):

        """Function:  test_ssl_config

        Description:  Test config with ssl attributes set.

        Arguments:

        """

        mysqldb = mysql_class.Server(
            self.name, self.server_id, self.sql_user, self.sql_pass,
            os_type=self.machine, ssl_client_ca="CAFile")

        self.assertEqual(mysqldb.config, self.config2)

    def test_ssl_verify_cert2(self):

        """Function:  test_ssl_verify_cert2

        Description:  Test with ssl_verify_cert attribute.

        Arguments:

        """

        mysqldb = mysql_class.Server(
            self.name, self.server_id, self.sql_user, self.sql_pass,
            os_type=self.machine, ssl_verify_cert=True)

        self.assertEqual(mysqldb.ssl_verify_cert, True)

    def test_ssl_verify_cert(self):

        """Function:  test_ssl_verify_cert

        Description:  Test with ssl_verify_cert attribute.

        Arguments:

        """

        mysqldb = mysql_class.Server(
            self.name, self.server_id, self.sql_user, self.sql_pass,
            os_type=self.machine)

        self.assertEqual(mysqldb.ssl_verify_cert, False)

    def test_ssl_verify_id2(self):

        """Function:  test_ssl_verify_id2

        Description:  Test with ssl_verify_id attribute.

        Arguments:

        """

        mysqldb = mysql_class.Server(
            self.name, self.server_id, self.sql_user, self.sql_pass,
            os_type=self.machine, ssl_verify_id=True)

        self.assertEqual(mysqldb.ssl_verify_id, True)

    def test_ssl_verify_id(self):

        """Function:  test_ssl_verify_id

        Description:  Test with ssl_verify_id attribute.

        Arguments:

        """

        mysqldb = mysql_class.Server(
            self.name, self.server_id, self.sql_user, self.sql_pass,
            os_type=self.machine)

        self.assertEqual(mysqldb.ssl_verify_id, False)

    def test_ssl_disabled2(self):

        """Function:  test_ssl_disabled2

        Description:  Test with ssl_disabled attribute.

        Arguments:

        """

        mysqldb = mysql_class.Server(
            self.name, self.server_id, self.sql_user, self.sql_pass,
            os_type=self.machine, ssl_disabled=True)

        self.assertEqual(mysqldb.ssl_disabled, True)

    def test_ssl_disabled(self):

        """Function:  test_ssl_disabled

        Description:  Test with ssl_disabled attribute.

        Arguments:

        """

        mysqldb = mysql_class.Server(
            self.name, self.server_id, self.sql_user, self.sql_pass,
            os_type=self.machine)

        self.assertEqual(mysqldb.ssl_disabled, False)

    def test_ssl_client_flag2(self):

        """Function:  test_ssl_client_flag2

        Description:  Test with ssl_client_flag attribute.

        Arguments:

        """

        mysqldb = mysql_class.Server(
            self.name, self.server_id, self.sql_user, self.sql_pass,
            os_type=self.machine, ssl_client_flag=4096)

        self.assertEqual(mysqldb.ssl_client_flag, 4096)

    def test_ssl_client_flag(self):

        """Function:  test_ssl_client_flag

        Description:  Test with ssl_client_flag attribute.

        Arguments:

        """

        mysqldb = mysql_class.Server(
            self.name, self.server_id, self.sql_user, self.sql_pass,
            os_type=self.machine)

        self.assertEqual(mysqldb.ssl_client_flag,
                         mysql.connector.ClientFlag.SSL)

    def test_ssl_client_cert2(self):

        """Function:  test_ssl_client_cert2

        Description:  Test with ssl_client_cert attribute.

        Arguments:

        """

        mysqldb = mysql_class.Server(
            self.name, self.server_id, self.sql_user, self.sql_pass,
            os_type=self.machine, ssl_client_cert="CertFile")

        self.assertEqual(mysqldb.ssl_client_cert, "CertFile")

    def test_ssl_client_cert(self):

        """Function:  test_ssl_client_cert

        Description:  Test with ssl_client_cert attribute.

        Arguments:

        """

        mysqldb = mysql_class.Server(
            self.name, self.server_id, self.sql_user, self.sql_pass,
            os_type=self.machine)

        self.assertEqual(mysqldb.ssl_client_cert, None)

    def test_ssl_client_key2(self):

        """Function:  test_ssl_client_key2

        Description:  Test with ssl_client_key attribute.

        Arguments:

        """

        mysqldb = mysql_class.Server(
            self.name, self.server_id, self.sql_user, self.sql_pass,
            os_type=self.machine, ssl_client_key="KeyFile")

        self.assertEqual(mysqldb.ssl_client_key, "KeyFile")

    def test_ssl_client_key(self):

        """Function:  test_ssl_client_key

        Description:  Test with ssl_client_key attribute.

        Arguments:

        """

        mysqldb = mysql_class.Server(
            self.name, self.server_id, self.sql_user, self.sql_pass,
            os_type=self.machine)

        self.assertEqual(mysqldb.ssl_client_key, None)

    def test_ssl_client_ca2(self):

        """Function:  test_ssl_client_ca2

        Description:  Test with ssl_client_ca attribute.

        Arguments:

        """

        mysqldb = mysql_class.Server(
            self.name, self.server_id, self.sql_user, self.sql_pass,
            os_type=self.machine, ssl_client_ca="CAFile")

        self.assertEqual(mysqldb.ssl_client_ca, "CAFile")

    def test_ssl_client_ca(self):

        """Function:  test_ssl_client_ca

        Description:  Test with ssl_client_ca attribute.

        Arguments:

        """

        mysqldb = mysql_class.Server(
            self.name, self.server_id, self.sql_user, self.sql_pass,
            os_type=self.machine)

        self.assertEqual(mysqldb.ssl_client_ca, None)

    def test_sql_pass(self):

        """Function:  test_sql_pass

        Description:  Test with sql_pass attribute.

        Arguments:

        """

        mysqldb = mysql_class.Server(
            self.name, self.server_id, self.sql_user, self.sql_pass,
            os_type=self.machine)

        self.assertEqual(mysqldb.sql_pass, self.sql_pass)

    def test_indb_buf_write(self):

        """Function:  test_indb_buf_write

        Description:  Test with indb_buf_write attribute.

        Arguments:

        """

        mysqldb = mysql_class.Server(
            self.name, self.server_id, self.sql_user, self.sql_pass,
            os_type=self.machine)

        self.assertEqual(mysqldb.indb_buf_write, None)

    def test_version(self):

        """Function:  test_version

        Description:  Test with version attribute.

        Arguments:

        """

        mysqldb = mysql_class.Server(
            self.name, self.server_id, self.sql_user, self.sql_pass,
            os_type=self.machine)

        self.assertEqual(mysqldb.version, None)

    def test_config(self):

        """Function:  test_config

        Description:  Test with config attribute.

        Arguments:

        """

        mysqldb = mysql_class.Server(
            self.name, self.server_id, self.sql_user, self.sql_pass,
            os_type=self.machine)

        self.assertEqual(mysqldb.config, self.config)

    def test_no_extra_def_file(self):

        """Function:  test_no_extra_def_file

        Description:  Test with no extra_def_file arg.

        Arguments:

        """

        mysqldb = mysql_class.Server(
            self.name, self.server_id, self.sql_user, self.sql_pass,
            os_type=self.machine)

        self.assertEqual(mysqldb.extra_def_file, None)

    def test_extra_def_file(self):

        """Function:  test_extra_def_file

        Description:  Test with passing extra_def_file arg.

        Arguments:

        """

        mysqldb = mysql_class.Server(
            self.name, self.server_id, self.sql_user, self.sql_pass,
            os_type=self.machine, extra_def_file=self.extra_def_file)

        self.assertEqual(
            (mysqldb.name, mysqldb.server_id, mysqldb.sql_user,
             mysqldb.sql_pass, mysqldb.machine, mysqldb.host,
             mysqldb.extra_def_file),
            (self.name, self.server_id, self.sql_user, self.sql_pass,
             self.machine, "localhost", self.extra_def_file))

    def test_no_port(self):

        """Function:  test_no_port

        Description:  Test with no port arg.

        Arguments:

        """

        mysqldb = mysql_class.Server(
            self.name, self.server_id, self.sql_user, self.sql_pass,
            os_type=self.machine)

        self.assertEqual(mysqldb.port, 3306)

    def test_port(self):

        """Function:  test_port

        Description:  Test with passing port arg.

        Arguments:

        """

        mysqldb = mysql_class.Server(
            self.name, self.server_id, self.sql_user, self.sql_pass,
            os_type=self.machine, port=self.port)

        self.assertEqual(
            (mysqldb.name, mysqldb.server_id, mysqldb.sql_user,
             mysqldb.sql_pass, mysqldb.machine, mysqldb.host, mysqldb.port),
            (self.name, self.server_id, self.sql_user, self.sql_pass,
             self.machine, "localhost", self.port))

    def test_no_host(self):

        """Function:  test_no_host

        Description:  Test with no host arg.

        Arguments:

        """

        mysqldb = mysql_class.Server(
            self.name, self.server_id, self.sql_user, self.sql_pass,
            os_type=self.machine)

        self.assertEqual(mysqldb.host, "localhost")

    def test_host(self):

        """Function:  test_host

        Description:  Test with passing host arg.

        Arguments:

        """

        mysqldb = mysql_class.Server(
            self.name, self.server_id, self.sql_user, self.sql_pass,
            os_type=self.machine, host=self.host)

        self.assertEqual(
            (mysqldb.name, mysqldb.server_id, mysqldb.sql_user,
             mysqldb.sql_pass, mysqldb.machine, mysqldb.host, mysqldb.port),
            (self.name, self.server_id, self.sql_user, self.sql_pass,
             self.machine, self.host, 3306))

    def test_no_default(self):

        """Function:  test_no_default

        Description:  Test with no default file.

        Arguments:

        """

        mysqldb = mysql_class.Server(
            self.name, self.server_id, self.sql_user, self.sql_pass,
            os_type=self.machine)

        self.assertEqual(mysqldb.defaults_file, self.results)

    def test_default(self):

        """Function:  test_default

        Description:  Test with default file.

        Arguments:

        """

        mysqldb = mysql_class.Server(
            self.name, self.server_id, self.sql_user, self.sql_pass,
            os_type=self.machine, defaults_file=self.defaults_file)

        self.assertEqual(
            (mysqldb.name, mysqldb.server_id, mysqldb.sql_user,
             mysqldb.sql_pass, mysqldb.machine, mysqldb.host, mysqldb.port),
            (self.name, self.server_id, self.sql_user, self.sql_pass,
             self.machine, "localhost", 3306))


if __name__ == "__main__":
    unittest.main()
