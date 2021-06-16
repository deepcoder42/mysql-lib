#!/usr/bin/python
# Classification (U)

"""Program:  server_setup_ssl.py

    Description:  Unit testing of Server.setup_ssl in mysql_class.py.

    Usage:
        test/unit/mysql_class/server_setup_ssl.py

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
        test_key_cert_yes_ca3 -> Test with cert and key present and with ca.
        test_key_cert_yes_ca2 -> Test with cert and key present and with ca.
        test_key_cert_yes_ca -> Test with cert and key present and with ca.
        test_key_cert_no_ca3 -> Test with cert and key present, but no ca.
        test_key_cert_no_ca2 -> Test with cert and key present, but no ca.
        test_key_cert_no_ca -> Test with cert and key present, but no ca.
        test_ssl_all2 -> Test with all ssl arguments present.
        test_ssl_all -> Test with all ssl arguments present.
        test_ssl_client_cert -> Test with ssl_client_cert only.
        test_ssl_client_key -> Test with ssl_client_key only.
        test_ssl_client_flag -> Test with ssl_client_flag present.
        test_ssl_client_key_cert3 -> Test with both cert and key present.
        test_ssl_client_key_cert2 -> Test with both cert and key present.
        test_ssl_client_key_cert -> Test with both cert and key present.
        test_ssl_client_ca3 -> Test with ssl_client_ca only present.
        test_ssl_client_ca2 -> Test with ssl_client_ca only present.
        test_ssl_client_ca -> Test with ssl_client_ca only present.

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
        self.port = 3306
        self.defaults_file = "def_cfg_file"
        self.extra_def_file = "extra_cfg_file"
        self.ssl_client_ca = "CAFile"
        self.ssl_client_key = "KeyFile"
        self.ssl_client_cert = "CertFile"
        self.ssl_client_flag = mysql.connector.ClientFlag.SSL

        self.config = {}
        self.config[key1 + key2] = self.sql_pass
        self.config["ssl_ca"] = "CAFile"
        self.config["client_flags"] = [mysql.connector.ClientFlag.SSL]
        self.config["ssl_disabled"] = False
        self.config["ssl_verify_identity"] = False
        self.config["ssl_verify_cert"] = False

        self.config2 = {}
        self.config2[key1 + key2] = self.sql_pass
        self.config2["ssl_key"] = "KeyFile"
        self.config2["ssl_cert"] = "CertFile"
        self.config2["client_flags"] = [mysql.connector.ClientFlag.SSL]
        self.config2["ssl_ca"] = ""
        self.config2["ssl_disabled"] = False
        self.config2["ssl_verify_identity"] = False

        self.config3 = {}
        self.config3[key1 + key2] = self.sql_pass
        self.config3["ssl_ca"] = "CAFile"
        self.config3["ssl_key"] = "KeyFile"
        self.config3["ssl_cert"] = "CertFile"
        self.config3["client_flags"] = [mysql.connector.ClientFlag.SSL]
        self.config3["ssl_disabled"] = False
        self.config3["ssl_verify_identity"] = False
        self.config3["ssl_verify_cert"] = False

    def test_key_cert_yes_ca3(self):

        """Function:  test_key_cert_yes_ca3

        Description:  Test with cert and key present and with ca.

        Arguments:

        """

        mysqldb = mysql_class.Server(
            self.name, self.server_id, self.sql_user, self.sql_pass,
            os_type=self.machine, ssl_client_key=self.ssl_client_key,
            ssl_client_cert=self.ssl_client_cert,
            ssl_client_ca=self.ssl_client_ca)
        mysqldb.setup_ssl(
            ssl_client_ca=self.ssl_client_ca,
            ssl_client_key=self.ssl_client_key,
            ssl_client_cert=self.ssl_client_cert,
            ssl_client_flag=self.ssl_client_flag)

        self.assertEqual(mysqldb.config, self.config3)

    def test_key_cert_yes_ca2(self):

        """Function:  test_key_cert_yes_ca2

        Description:  Test with cert and key present and with ca.

        Arguments:

        """

        mysqldb = mysql_class.Server(
            self.name, self.server_id, self.sql_user, self.sql_pass,
            os_type=self.machine, ssl_client_key=self.ssl_client_key,
            ssl_client_cert=self.ssl_client_cert,
            ssl_client_ca=self.ssl_client_ca)
        mysqldb.setup_ssl(
            ssl_client_ca=self.ssl_client_ca,
            ssl_client_key=self.ssl_client_key,
            ssl_client_cert=self.ssl_client_cert,
            ssl_client_flag=self.ssl_client_flag)

        self.assertEqual(
            (mysqldb.ssl_client_ca, mysqldb.ssl_client_flag),
            (self.ssl_client_ca, mysql.connector.ClientFlag.SSL))

    def test_key_cert_yes_ca(self):

        """Function:  test_key_cert_yes_ca

        Description:  Test with cert and key present and with ca.

        Arguments:

        """

        mysqldb = mysql_class.Server(
            self.name, self.server_id, self.sql_user, self.sql_pass,
            os_type=self.machine, ssl_client_key=self.ssl_client_key,
            ssl_client_cert=self.ssl_client_cert,
            ssl_client_ca=self.ssl_client_ca)
        mysqldb.setup_ssl(
            ssl_client_ca=self.ssl_client_ca,
            ssl_client_key=self.ssl_client_key,
            ssl_client_cert=self.ssl_client_cert,
            ssl_client_flag=self.ssl_client_flag)

        self.assertEqual(
            (mysqldb.ssl_client_key, mysqldb.ssl_client_cert),
            (self.ssl_client_key, self.ssl_client_cert))

    def test_key_cert_no_ca3(self):

        """Function:  test_key_cert_no_ca3

        Description:  Test with cert and key present, but no ca.

        Arguments:

        """

        mysqldb = mysql_class.Server(
            self.name, self.server_id, self.sql_user, self.sql_pass,
            os_type=self.machine, ssl_client_key=self.ssl_client_key,
            ssl_client_cert=self.ssl_client_cert)
        mysqldb.setup_ssl(
            ssl_client_key=self.ssl_client_key,
            ssl_client_cert=self.ssl_client_cert,
            ssl_client_flag=self.ssl_client_flag)

        self.assertEqual(mysqldb.config, self.config2)

    def test_key_cert_no_ca2(self):

        """Function:  test_key_cert_no_ca2

        Description:  Test with cert and key present, but no ca.

        Arguments:

        """

        mysqldb = mysql_class.Server(
            self.name, self.server_id, self.sql_user, self.sql_pass,
            os_type=self.machine, ssl_client_key=self.ssl_client_key,
            ssl_client_cert=self.ssl_client_cert)
        mysqldb.setup_ssl(
            ssl_client_key=self.ssl_client_key,
            ssl_client_cert=self.ssl_client_cert,
            ssl_client_flag=self.ssl_client_flag)

        self.assertEqual(
            (mysqldb.ssl_client_ca, mysqldb.ssl_client_flag),
            (None, mysql.connector.ClientFlag.SSL))

    def test_key_cert_no_ca(self):

        """Function:  test_key_cert_no_ca

        Description:  Test with cert and key present, but no ca.

        Arguments:

        """

        mysqldb = mysql_class.Server(
            self.name, self.server_id, self.sql_user, self.sql_pass,
            os_type=self.machine, ssl_client_key=self.ssl_client_key,
            ssl_client_cert=self.ssl_client_cert)
        mysqldb.setup_ssl(
            ssl_client_key=self.ssl_client_key,
            ssl_client_cert=self.ssl_client_cert,
            ssl_client_flag=self.ssl_client_flag)

        self.assertEqual(
            (mysqldb.ssl_client_key, mysqldb.ssl_client_cert),
            (self.ssl_client_key, self.ssl_client_cert))

    def test_ssl_all2(self):

        """Function:  test_ssl_all2

        Description:  Test with all ssl arguments present.

        Arguments:

        """

        mysqldb = mysql_class.Server(
            self.name, self.server_id, self.sql_user, self.sql_pass,
            os_type=self.machine)
        mysqldb.setup_ssl(
            ssl_client_ca=self.ssl_client_ca,
            ssl_client_key=self.ssl_client_key,
            ssl_client_cert=self.ssl_client_cert,
            ssl_client_flag=self.ssl_client_flag)

        self.assertEqual(mysqldb.config, self.config3)

    def test_ssl_all(self):

        """Function:  test_ssl_all

        Description:  Test with all ssl arguments present.

        Arguments:

        """

        mysqldb = mysql_class.Server(
            self.name, self.server_id, self.sql_user, self.sql_pass,
            os_type=self.machine)
        mysqldb.setup_ssl(
            ssl_client_ca=self.ssl_client_ca,
            ssl_client_key=self.ssl_client_key,
            ssl_client_cert=self.ssl_client_cert,
            ssl_client_flag=self.ssl_client_flag)

        self.assertEqual(
            (mysqldb.ssl_client_ca, mysqldb.ssl_client_key,
             mysqldb.ssl_client_cert, mysqldb.ssl_client_flag),
            (self.ssl_client_ca, self.ssl_client_key, self.ssl_client_cert,
             self.ssl_client_flag))

    def test_ssl_client_cert(self):

        """Function:  test_ssl_client_cert

        Description:  Test with ssl_client_cert present.

        Arguments:

        """

        mysqldb = mysql_class.Server(
            self.name, self.server_id, self.sql_user, self.sql_pass,
            os_type=self.machine)
        mysqldb.setup_ssl(ssl_client_cert=self.ssl_client_cert)

        self.assertEqual(mysqldb.ssl_client_cert, self.ssl_client_cert)

    def test_ssl_client_key(self):

        """Function:  test_ssl_client_key

        Description:  Test with ssl_client_key present.

        Arguments:

        """

        mysqldb = mysql_class.Server(
            self.name, self.server_id, self.sql_user, self.sql_pass,
            os_type=self.machine)
        mysqldb.setup_ssl(ssl_client_key=self.ssl_client_key)

        self.assertEqual(mysqldb.ssl_client_key, self.ssl_client_key)

    def test_ssl_client_flag(self):

        """Function:  test_ssl_client_flag

        Description:  Test with ssl_client_flag present.

        Arguments:

        """

        mysqldb = mysql_class.Server(
            self.name, self.server_id, self.sql_user, self.sql_pass,
            os_type=self.machine)
        mysqldb.setup_ssl(ssl_client_flag=self.ssl_client_flag)

        self.assertEqual(mysqldb.ssl_client_flag, self.ssl_client_flag)

    def test_ssl_client_key_cert3(self):

        """Function:  test_ssl_client_key_cert3

        Description:  Test with both cert and key present.

        Arguments:

        """

        mysqldb = mysql_class.Server(
            self.name, self.server_id, self.sql_user, self.sql_pass,
            os_type=self.machine)
        mysqldb.setup_ssl(ssl_client_key=self.ssl_client_key,
                          ssl_client_cert=self.ssl_client_cert)

        self.assertEqual(mysqldb.config, self.config2)

    def test_ssl_client_key_cert2(self):

        """Function:  test_ssl_client_key_cert2

        Description:  Test with both cert and key present.

        Arguments:

        """

        mysqldb = mysql_class.Server(
            self.name, self.server_id, self.sql_user, self.sql_pass,
            os_type=self.machine)
        mysqldb.setup_ssl(ssl_client_key=self.ssl_client_key,
                          ssl_client_cert=self.ssl_client_cert)

        self.assertEqual(
            (mysqldb.ssl_client_ca, mysqldb.ssl_client_flag),
            (None, mysql.connector.ClientFlag.SSL))

    def test_ssl_client_key_cert(self):

        """Function:  test_ssl_client_key_cert

        Description:  Test with both cert and key present.

        Arguments:

        """

        mysqldb = mysql_class.Server(
            self.name, self.server_id, self.sql_user, self.sql_pass,
            os_type=self.machine)
        mysqldb.setup_ssl(ssl_client_key=self.ssl_client_key,
                          ssl_client_cert=self.ssl_client_cert)

        self.assertEqual(
            (mysqldb.ssl_client_key, mysqldb.ssl_client_cert),
            (self.ssl_client_key, self.ssl_client_cert))

    def test_ssl_client_ca3(self):

        """Function:  test_ssl_client_flag

        Description:  Test with ssl_client_ca only present.

        Arguments:

        """

        mysqldb = mysql_class.Server(
            self.name, self.server_id, self.sql_user, self.sql_pass,
            os_type=self.machine)
        mysqldb.setup_ssl(ssl_client_ca=self.ssl_client_ca)

        self.assertEqual(mysqldb.config, self.config)

    def test_ssl_client_ca2(self):

        """Function:  test_ssl_client_flag2

        Description:  Test with ssl_client_ca only present.

        Arguments:

        """

        mysqldb = mysql_class.Server(
            self.name, self.server_id, self.sql_user, self.sql_pass,
            os_type=self.machine)
        mysqldb.setup_ssl(ssl_client_ca=self.ssl_client_ca)

        self.assertEqual(
            (mysqldb.ssl_client_key, mysqldb.ssl_client_cert,
             mysqldb.ssl_client_flag),
            (None, None, mysql.connector.ClientFlag.SSL))

    def test_ssl_client_ca(self):

        """Function:  test_ssl_client_flag

        Description:  Test with ssl_client_ca only present.

        Arguments:

        """

        mysqldb = mysql_class.Server(
            self.name, self.server_id, self.sql_user, self.sql_pass,
            os_type=self.machine)
        mysqldb.setup_ssl(ssl_client_ca=self.ssl_client_ca)

        self.assertEqual(mysqldb.ssl_client_ca, self.ssl_client_ca)


if __name__ == "__main__":
    unittest.main()
