#!/usr/bin/python3
"""Unittests for User class."""
import unittest
from models.user import User
import datetime


class TestUser(unittest.TestCase):
    """Test cases for the User class."""

    def test_init(self):
        """Test initialization of User."""
        u = User()
        self.assertIsInstance(u, User)
        self.assertIsInstance(u.id, str)
        self.assertIsInstance(u.created_at, datetime.datetime)
        self.assertIsInstance(u.updated_at, datetime.datetime)
        self.assertEqual(u.email, "")
        self.assertEqual(u.password, "")
        self.assertEqual(u.first_name, "")
        self.assertEqual(u.last_name, "")


if __name__ == "__main__":
    unittest.main()
