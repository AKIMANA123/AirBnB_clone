#!/usr/bin/python3
"""Unittests for City class."""
import unittest
from models.city import City
import datetime


class TestCity(unittest.TestCase):
    """Test cases for the City class."""

    def test_init(self):
        """Test initialization of City."""
        c = City()
        self.assertIsInstance(c, City)
        self.assertIsInstance(c.id, str)
        self.assertEqual(c.state_id, "")
        self.assertEqual(c.name, "")


if __name__ == "__main__":
    unittest.main()
