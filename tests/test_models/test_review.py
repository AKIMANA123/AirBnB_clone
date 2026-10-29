#!/usr/bin/python3
"""Unittests for Review class."""
import unittest
from models.review import Review


class TestReview(unittest.TestCase):
    """Test cases for the Review class."""

    def test_init(self):
        """Test initialization of Review."""
        r = Review()
        self.assertIsInstance(r, Review)
        self.assertEqual(r.place_id, "")
        self.assertEqual(r.user_id, "")
        self.assertEqual(r.text, "")


if __name__ == "__main__":
    unittest.main()
