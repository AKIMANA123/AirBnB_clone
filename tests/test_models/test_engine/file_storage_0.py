#!/usr/bin/python3
"""Test FileStorage __file_path"""
import unittest
from models.engine.file_storage import FileStorage


class TestFileStorageFilePath(unittest.TestCase):
    """Test __file_path attribute"""
    def test_file_path(self):
        """Check __file_path exists and is a string"""
        storage = FileStorage()
        self.assertTrue(hasattr(storage, "_FileStorage__file_path"))
        self.assertIsInstance(storage._FileStorage__file_path, str)


if __name__ == "__main__":
    unittest.main()
