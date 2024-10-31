import unittest
import pandas as pd
import os
#import sys

#sys.path.insert(1,os.getcwd())
#from scripts.import_data import parse_data

def parse_data(path='Experimental_data'):
    dict = {}
    dir = os.listdir(path)
    for filename in dir:
        print(path + '/' + filename)
        data = pd.read_excel(path + '/' + filename)
        dict[filename] = data
    return dict
class TestImport(unittest.TestCase):

    def test_type(self):
        """Test that parse_data returns dict type"""
        self.assertTrue(isinstance(parse_data(), dict))

# test = TestImport()
# test.test_type()
