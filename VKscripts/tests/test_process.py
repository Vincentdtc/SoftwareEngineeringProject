import unittest
import VKscripts as vk

class TestImport2(unittest.TestCase):

    def test_type2(self):
        """Test that parse_data returns dict type"""
        input = vk.import_data.parse_data()
        self.assertTrue(isinstance(vk.Process_data.process_data(input), dict))
