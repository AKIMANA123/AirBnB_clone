#!/usr/bin/python3
"""Test FileStorage new()"""
import unittest
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel


class TestFileStorageNew(unittest.TestCase):
    """Test new method"""
    def test_new(self):
        """Check new adds object"""
        storage = FileStorage()
        bm = BaseModel()
        storage.new(bm)
        key = "BaseModel.{}".format(bm.id)
        self.assertIn(key, storage.all())


if __name__ == "__main__":
    unittest.main()
