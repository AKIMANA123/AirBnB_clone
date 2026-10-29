#!/usr/bin/python3
"""Test BaseModel save(self)"""
import unittest
from models.base_model import BaseModel
import datetime


class TestBaseModelSave(unittest.TestCase):
    """Test save method of BaseModel"""
    def test_save(self):
        """Check save updates updated_at"""
        bm = BaseModel()
        old_updated = bm.updated_at
        bm.save()
        self.assertNotEqual(old_updated, bm.updated_at)


if __name__ == "__main__":
    unittest.main()
