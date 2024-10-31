import unittest
import VKscripts as vk

class TestImport(unittest.TestCase):

    def test_type(self):
        """Test that parse_data returns dict type"""
        self.assertTrue(isinstance(vk.Process_data.process_data(), dict))
