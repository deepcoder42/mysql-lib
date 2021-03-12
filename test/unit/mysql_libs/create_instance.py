#!/usr/bin/python
# Classification (U)

"""Program:  create_instance.py

    Description:  Unit testing of create_instance in mysql_libs.py.

    Usage:
        test/unit/mysql_libs/create_instance.py

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
import mysql_libs
import version

__version__ = version.__version__


class SlaveRep(object):

    """Class:  SlaveRep

    Description:  Class stub holder for SlaveRep class.

    Methods:
        __init__ -> Class initialization.

    """

    def __init__(self, name, sid, user, japd, **kwargs):

        """Method:  __init__

        Description:  Class initialization.

        Arguments:

        """

        self.name = name
        self.sid = sid
        self.user = user
        self.japd = japd
        self.serv_os = kwargs.get("machine")
        self.host = kwargs.get("host")
        self.port = kwargs.get("port")
        self.cfg_file = kwargs.get("defaults_file")
        self.extra_def_file = kwargs.get("extra_def_file", None)
        self.rep_user = kwargs.get("rep_user", None)
        self.rep_japd = kwargs.get("rep_japd", None)


class Server(object):

    """Class:  Server

    Description:  Class stub holder for Server class.

    Methods:
        __init__ -> Class initialization.

    """

    def __init__(self, name, sid, user, japd, **kwargs):

        """Method:  __init__

        Description:  Class initialization.

        Arguments:

        """

        self.name = name
        self.sid = sid
        self.user = user
        self.japd = japd
        self.serv_os = kwargs.get("machine")
        self.host = kwargs.get("host")
        self.port = kwargs.get("port")
        self.cfg_file = kwargs.get("defaults_file")
        self.extra_def_file = kwargs.get("extra_def_file", None)


class Cfg(object):

    """Class:  Cfg

    Description:  Stub holder for configuration file.

    Methods:
        __init__ -> Class initialization.

    """

    def __init__(self):

        """Method:  __init__

        Description:  Class initialization.

        Arguments:

        """

        self.name = "name"
        self.sid = "sid"
        self.user = "user"
        self.japd = None
        self.serv_os = "Linux"
        self.host = "hostname"
        self.port = 3306
        self.cfg_file = "cfg_file"
        self.extra_def_file = "extra_def_file"


class Cfg2(object):

    """Class:  Cfg2

    Description:  Stub holder for configuration file.

    Methods:
        __init__ -> Class initialization.

    """

    def __init__(self):

        """Method:  __init__

        Description:  Class initialization.

        Arguments:

        """

        self.name = "name"
        self.sid = "sid"
        self.user = "user"
        self.japd = None
        self.serv_os = "Linux"
        self.host = "hostname"
        self.port = 3306
        self.cfg_file = "cfg_file"
        self.extra_def_file = "extra_def_file"
        self.rep_user = "rep_user"
        self.rep_japd = "rep_japd"


class UnitTest(unittest.TestCase):

    """Class:  UnitTest

    Description:  Class which is a representation of a unit testing.

    Methods:
        setUp -> Initialize testing environment.
        test_rep_user2 -> Test with for rep_user.
        test_rep_user -> Test with for rep_user.
        test_none_rep_user2 -> Test with none for rep_user.
        test_none_rep_user -> Test with none for rep_user.
        test_none_extra_def_file2 -> Test with none for extra_def_file.
        test_none_extra_def_file -> Test with none for extra_def_file.
        test_create_instance -> Test create_instance function.

    """

    def setUp(self):

        """Function:  setUp

        Description:  Initialization for unit testing.

        Arguments:

        """

        self.cfg = Cfg()
        self.cfg2 = Cfg2()
        self.name = "name"
        self.sid = "sid"
        self.user = "user"
        self.japd = None
        self.serv_os = "Linux"
        self.host = "hostname"
        self.port = 3306
        self.cfg_file = "cfg_file"
        self.extra_def_file = "extra_def_file"
        self.server = Server(
            self.name, self.sid, self.user, self.japd, machine=self.serv_os,
            host=self.host, port=self.port, defaults_file=self.cfg_file)

    @mock.patch("mysql_libs.gen_libs.load_module")
    def test_rep_user2(self, mock_cfg):

        """Function:  test_rep_user2

        Description:  Test with for rep_user.

        Arguments:

        """

        mock_cfg.return_value = self.cfg2

        srv_inst = mysql_libs.create_instance("Cfgfile", "DirPath", SlaveRep)

        self.assertEqual(srv_inst.__dict__.get("rep_user", None),
                         self.cfg2.rep_user)

    @mock.patch("mysql_libs.gen_libs.load_module")
    def test_rep_user(self, mock_cfg):

        """Function:  test_rep_user

        Description:  Test with for rep_user.

        Arguments:

        """

        mock_cfg.return_value = self.cfg2

        srv_inst = mysql_libs.create_instance("Cfgfile", "DirPath", SlaveRep)

        self.assertTrue(isinstance(srv_inst, SlaveRep))

    @mock.patch("mysql_libs.gen_libs.load_module")
    def test_none_rep_user2(self, mock_cfg):

        """Function:  test_none_rep_user2

        Description:  Test with none for rep_user.

        Arguments:

        """

        mock_cfg.return_value = self.cfg

        srv_inst = mysql_libs.create_instance("Cfgfile", "DirPath", Server)

        self.assertEqual(srv_inst.__dict__.get("rep_user", None), None)

    @mock.patch("mysql_libs.gen_libs.load_module")
    def test_none_rep_user(self, mock_cfg):

        """Function:  test_none_rep_user

        Description:  Test with none for rep_user.

        Arguments:

        """

        mock_cfg.return_value = self.cfg

        srv_inst = mysql_libs.create_instance("Cfgfile", "DirPath", Server)

        self.assertTrue(isinstance(srv_inst, Server))

    @mock.patch("mysql_libs.gen_libs.load_module")
    def test_none_extra_def_file2(self, mock_cfg):

        """Function:  test_none_extra_def_file2

        Description:  Test with none for extra_def_file.

        Arguments:

        """

        mock_cfg.return_value = self.cfg
        self.cfg.extra_def_file = None

        srv_inst = mysql_libs.create_instance("Cfgfile", "DirPath", Server)

        self.assertEqual(srv_inst.extra_def_file, None)

    @mock.patch("mysql_libs.gen_libs.load_module")
    def test_none_extra_def_file(self, mock_cfg):

        """Function:  test_none_extra_def_file

        Description:  Test with none for extra_def_file.

        Arguments:

        """

        mock_cfg.return_value = self.cfg
        self.cfg.extra_def_file = None

        srv_inst = mysql_libs.create_instance("Cfgfile", "DirPath", Server)

        self.assertTrue(isinstance(srv_inst, Server))

    @mock.patch("mysql_libs.gen_libs.load_module")
    def test_create_instance(self, mock_cfg):

        """Function:  test_create_instance

        Description:  Test create_instance function.

        Arguments:

        """

        mock_cfg.return_value = self.cfg

        srv_inst = mysql_libs.create_instance("Cfgfile", "DirPath", Server)

        self.assertTrue(isinstance(srv_inst, Server))


if __name__ == "__main__":
    unittest.main()
