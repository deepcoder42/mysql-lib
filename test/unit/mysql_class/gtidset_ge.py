#!/usr/bin/python
# Classification (U)

"""Program:  gtidset_ge.py

    Description:  Unit testing of GTIDSet.__ge__ in mysql_class.py.

    Usage:
        test/unit/mysql_class/gtidset_ge.py

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
        test_gtidset_ge_true -> Test GTIDSet.__ge__ method for True return.
        test_gtidset_ge_equal -> Test GTIDSet.__ge__ for equal values.
        test_gtidset_ge_false -> Test GTIDSet.__ge__ method for False return.

    """

    def setUp(self):

        """Function:  setUp

        Description:  Initialization for unit testing.

        Arguments:

        """

        self.gtidset1 = "35588520:333217-740055"
        self.gtidset2 = "35588520:1-740055,76012896:1-502108"

    def test_gtidset_ge_true(self):

        """Function:  test_gtidset_ge_true

        Description:  Test GTIDSet.__ge__ method for True return.

        Arguments:

        """

        gtid1 = mysql_class.GTIDSet(self.gtidset1)
        gtid2 = mysql_class.GTIDSet(self.gtidset2)

        self.assertTrue(gtid2 >= gtid1)

    def test_gtidset_ge_equal(self):

        """Function:  test_gtidset_ge_equal

        Description:  Test GTIDSet.__ge__ for equal values.

        Arguments:

        """

        gtid1 = mysql_class.GTIDSet(self.gtidset1)
        gtid2 = mysql_class.GTIDSet(self.gtidset1)

        self.assertTrue(gtid1 >= gtid2)

    def test_gtidset_ge_false(self):

        """Function:  test_gtidset_ge_false

        Description:  Test GTIDSet.__ge__ method for False return.

        Arguments:

        """

        gtid1 = mysql_class.GTIDSet(self.gtidset1)
        gtid2 = mysql_class.GTIDSet(self.gtidset2)

        self.assertFalse(gtid1 >= gtid2)


if __name__ == "__main__":
    unittest.main()
