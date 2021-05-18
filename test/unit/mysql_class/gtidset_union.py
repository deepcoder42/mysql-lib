#!/usr/bin/python
# Classification (U)

"""Program:  gtidset_union.py

    Description:  Unit testing of GTIDSet.union in mysql_class.py.

    Usage:
        test/unit/mysql_class/gtidset_union.py

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
        test_not_gtidset -> Test GTIDSet.union method with non-GTIDSet.
        test_gtidset_union -> Test GTIDSet.union method.

    """

    def setUp(self):

        """Function:  setUp

        Description:  Initialization for unit testing.

        Arguments:

        """

        self.gtidset1 = "35588520:333217-740055"
        self.gtidset2 = "35588520:1-740055,76012896:1-502108"
        self.results = {"35588520": [(1, 740055)], "76012896": [(1, 502108)]}

    def test_not_gtidset(self):

        """Function:  test_not_gtidset

        Description:  Test GTIDSet.union method with non-GTIDSet.

        Arguments:

        """

        gtid1 = mysql_class.GTIDSet(self.gtidset1)
        gtid1.union(self.gtidset2)

        self.assertEqual(gtid1.gtids, self.results)

    def test_gtidset_union(self):

        """Function:  test_gtidset_union

        Description:  Test GTIDSet.union method.

        Arguments:

        """

        gtid1 = mysql_class.GTIDSet(self.gtidset1)
        gtid2 = mysql_class.GTIDSet(self.gtidset2)
        gtid1.union(gtid2)

        self.assertEqual(gtid1.gtids, self.results)


if __name__ == "__main__":
    unittest.main()
