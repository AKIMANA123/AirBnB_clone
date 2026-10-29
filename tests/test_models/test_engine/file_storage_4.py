#!/usr/bin/python3
"""Test FileStorage save()"""
import unittest
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel
import os


class TestFileStorageSave(unittest.TestCase):
    """Test save method"""
    def test_save(self):
        """Check save creates file"""
        storage = FileStorage()
        bm = BaseModel()
        storage.new(bm)
        storage.save()
        self.assertTrue(os.path.exists("file.json"))


if __name__ == "__main__":
    unittest.main()
