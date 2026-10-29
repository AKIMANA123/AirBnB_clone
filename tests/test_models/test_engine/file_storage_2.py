#!/usr/bin/python3
"""Test FileStorage all()"""
import unittest
from models.engine.file_storage import FileStorage


class TestFileStorageAll(unittest.TestCase):
    """Test all method"""
    def test_all(self):
        """Check all returns dict"""
        storage = FileStorage()
        self.assertIsInstance(storage.all(), dict)


if __name__ == "__main__":
    unittest.main()
