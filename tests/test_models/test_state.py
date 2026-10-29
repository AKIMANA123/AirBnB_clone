#!/usr/bin/python3
"""Unittests for State class."""
import unittest
from models.state import State
import datetime


class TestState(unittest.TestCase):
    """Test cases for the State class."""

    def test_init(self):
        """Test initialization of State."""
        s = State()
        self.assertIsInstance(s, State)
        self.assertIsInstance(s.id, str)
        self.assertEqual(s.name, "")


if __name__ == "__main__":
    unittest.main()
