import unittest
import VKscripts as vk

class TestImport3(unittest.TestCase):

    def test_type3(self):
        """Test that parse_data returns dict type"""
        input = vk.import_data.parse_data()
        data = vk.Process_data.process_data(input)
        self.assertTrue(isinstance(vk.visualise.create_fig(data), type(None)))
