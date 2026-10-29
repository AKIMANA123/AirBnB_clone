#!/usr/bin/python3
"""Unittests for FileStorage class."""
import unittest
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel
import os


class TestFileStorage(unittest.TestCase):
    """Test cases for the FileStorage class."""

    def test_all(self):
        """Test that all returns __objects dictionary."""
        storage = FileStorage()
        obj_dict = storage.all()
        self.assertIsInstance(obj_dict, dict)

    def test_new(self):
        """Test new adds objects to __objects."""
        storage = FileStorage()
        bm = BaseModel()
        storage.new(bm)
        key = "BaseModel.{}".format(bm.id)
        self.assertIn(key, storage.all())


if __name__ == "__main__":
    unittest.main()
