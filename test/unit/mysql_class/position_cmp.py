#!/usr/bin/python
# Classification (U)

"""Program:  position_cmp.py

    Description:  Unit testing of Position.__cmp__ in mysql_class.py.

    Usage:
        test/unit/mysql_class/position_cmp.py

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
import version

__version__ = version.__version__


class UnitTest(unittest.TestCase):

    """Class:  UnitTest

    Description:  Class which is a representation of a unit testing.

    Methods:
        setUp -> Initialize testing environment.
        test_positions_not_equal -> Test with positions not equal.
        test_positions_equal -> Test with positions equal.

    """

    def setUp(self):

        """Function:  setUp

        Description:  Initialization for unit testing.

        Arguments:

        """

        self.fname = "mysql-bin.01111"
        self.file1 = self.fname
        self.pos1 = 23489
        self.file2 = self.fname
        self.pos2 = 23482
        self.file3 = self.fname
        self.pos3 = 23489

    def test_positions_not_equal(self):

        """Function:  test_positions_not_equal

        Description:  Test with positions not equal.

        Arguments:

        """

        position1 = mysql_class.Position(self.file1, self.pos1)
        position3 = mysql_class.Position(self.file3, self.pos3)

        self.assertTrue(position1 == position3)

    def test_positions_equal(self):

        """Function:  test_positions_equal

        Description:  Test with positions equal.

        Arguments:

        """

        position1 = mysql_class.Position(self.file1, self.pos1)
        position3 = mysql_class.Position(self.file3, self.pos3)

        self.assertTrue(position1 == position3)


if __name__ == "__main__":
    unittest.main()
