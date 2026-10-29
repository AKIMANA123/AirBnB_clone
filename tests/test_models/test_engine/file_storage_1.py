#!/usr/bin/python3
"""Test FileStorage __objects"""
import unittest
from models.engine.file_storage import FileStorage


class TestFileStorageObjects(unittest.TestCase):
    """Test __objects attribute"""
    def test_objects(self):
        """Check __objects exists and is a dict"""
        storage = FileStorage()
        self.assertTrue(hasattr(storage, "_FileStorage__objects"))
        self.assertIsInstance(storage._FileStorage__objects, dict)


if __name__ == "__main__":
    unittest.main()
