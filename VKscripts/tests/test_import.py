import unittest
import os

import VKscripts as vk

class TestImport(unittest.TestCase):

    def test_type(self):
        """Test that parse_data returns dict type"""
        self.assertTrue(isinstance(vk.import_data.parse_data(), dict))
