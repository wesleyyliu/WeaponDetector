import unittest
from unittest.mock import Mock
from app import Detector
import os

class TestDetector(unittest.TestCase):
    def test_file_extensions_allowed(self):
        d = Detector("upload", ['.jpeg', '.jpg', '.mp4'])
        self.assertTrue(d.is_file_allowed('thisisallowed.jpeg'))
        self.assertTrue(d.is_file_allowed('thisisallowed.jpg'))
        self.assertTrue(d.is_file_allowed('thisisallowed.mp4'))
    
    def test_file_extensions_not_allowed(self):
        d = Detector("upload", ['.jpeg', '.jpg', '.mp4'])
        self.assertFalse(d.is_file_allowed('thisisnotallowed.gif'))
        self.assertFalse(d.is_file_allowed(''))

    def test_save_file_successful(self):
        d = Detector('uploads', ['.jpg', '.jpeg', '.mp4'])
        mock_file = Mock()
        mock_file.filename = 'test.jpg'
        saved_path = d.save_file(mock_file)
        expected_path = os.path.join('uploads', 'test.jpg')
        self.assertEqual(saved_path, expected_path)

    def test_save_file_fail_extension(self):
        d = Detector('uploads', ['.jpg', '.jpeg', '.mp4'])
        mock_file = Mock()
        mock_file.filename = 'test.gif'
        result = d.save_file(mock_file)
        self.assertIsNone(result)
   
if __name__ == "__main__":
    unittest.main()
