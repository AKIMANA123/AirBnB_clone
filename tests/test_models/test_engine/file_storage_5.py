#!/usr/bin/python3
"""Test FileStorage reload()"""
import unittest
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel
import os


class TestFileStorageReload(unittest.TestCase):
    """Test reload method"""
    def test_reload(self):
        """Check reload restores objects"""
        storage = FileStorage()
        bm = BaseModel()
        storage.new(bm)
        storage.save()
        storage._FileStorage__objects = {}
        storage.reload()
        key = "BaseModel.{}".format(bm.id)
        self.assertIn(key, storage.all())


if __name__ == "__main__":
    unittest.main()
