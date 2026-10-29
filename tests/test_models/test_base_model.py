#!/usr/bin/python3
"""Unittests for BaseModel class."""
import unittest
from models.base_model import BaseModel
import datetime


class TestBaseModel(unittest.TestCase):
    """Test cases for the BaseModel class."""

    def test_init(self):
        """Test initialization of BaseModel."""
        bm = BaseModel()
        self.assertIsInstance(bm, BaseModel)
        self.assertIsInstance(bm.id, str)
        self.assertIsInstance(bm.created_at, datetime.datetime)
        self.assertIsInstance(bm.updated_at, datetime.datetime)

    def test_save(self):
        """Test save method updates updated_at."""
        bm = BaseModel()
        old_updated = bm.updated_at
        bm.save()
        self.assertNotEqual(old_updated, bm.updated_at)

    def test_to_dict(self):
        """Test to_dict method returns proper dictionary."""
        bm = BaseModel()
        bm_dict = bm.to_dict()
        self.assertEqual(bm_dict["__class__"], "BaseModel")
        self.assertIsInstance(bm_dict["created_at"], str)
        self.assertIsInstance(bm_dict["updated_at"], str)


if __name__ == "__main__":
    unittest.main()
