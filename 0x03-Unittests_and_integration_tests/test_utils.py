#!/usr/bin/env python3
"""Unittests for utils.py"""
import unittest
from unittest.mock import patch
from parameterized import parameterized
from client import get_user, get_user_followers, get_user_following
from utils import get_user_data, get_user_followers_data, get_user_following_data


class TestUtils(unittest.TestCase):
    @parameterized.expand([
        ("get_user_data", "https://api.github.com/users/"),
        ("get_user_followers_data", "https://api.github.com/users/"),
        ("get_user_following_data", "https://api.github.com/users/")
    ])
    @patch('utils.requests.get')
    def test_get_user_data(self, mock_get, test_name, url):
        get_user_data(url)
        mock_get.assert_called_once_with(url)

    @patch('utils.requests.get')
    def test_get_user_followers_data(self, mock_get):
        get_user_followers_data("https://api.github.com/users/")
        mock_get.assert_called_once_with("https://api.github.com/users/")

    @patch('utils.requests.get')
    def test_get_user_following_data(self, mock_get):
        get_user_following_data("https://api.github.com/users/")
        mock_get.assert_called_once_with("https://api.github.com/users/")

if __name__ == '__main__':
    unittest.main()
