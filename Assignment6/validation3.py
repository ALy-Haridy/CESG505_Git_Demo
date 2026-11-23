"""
HOW TO run this test:

From the command line:
    execute
    $ python -m unittest -v validation2.py

    You may need to execute python3 (or python3.exe on Windows)

From PyCharm:
    1) under menu item "Run" select "Run" to run validation2 once
    2) under menu item "Run" select "Edit configuration"
    3) in the "Parameters" field, enter -v
    4) run again in PyCharm
"""

import unittest

from plateelement import *

class TestPlateElement(unittest.TestCase):

    def setUp(self):
        # define sample values
        f = open('examples.csv','r')

        # you need to read and organize the test cases
        self.tests = []
        for line in f:
            pass   # ... THIS IS YOUR JOB

        f.close()

    def test_F1(self):
        # your job to implement this test
        raise NotImplementedError

    def test_F2(self):
        # your job to implement this test
        raise NotImplementedError

    def test_F3(self):
        # your job to implement this test
        raise NotImplementedError

if __name__ == '__main__':
    unittest.main()