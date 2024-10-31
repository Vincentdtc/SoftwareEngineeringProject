import unittest
import os
import sys

sys.path.insert(1,os.getcwd())
from scripts.import_data import parse_data

class TestImport(unittest.TestCase):
    def test_type(self):
        """Test that parse_data returns dict type"""
        self.assertTrue(isinstance(parse_data(), dict))

test = TestImport()
test.test_type()
