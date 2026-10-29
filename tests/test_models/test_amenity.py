#!/usr/bin/python3
"""Unittests for Amenity class."""
import unittest
from models.amenity import Amenity


class TestAmenity(unittest.TestCase):
    """Test cases for the Amenity class."""

    def test_init(self):
        """Test initialization of Amenity."""
        a = Amenity()
        self.assertIsInstance(a, Amenity)
        self.assertEqual(a.name, "")


if __name__ == "__main__":
    unittest.main()
