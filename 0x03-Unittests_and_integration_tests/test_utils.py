#!/usr/bin/env python3
"""Unittests for utils.py"""
import unittest
from typing import Dict, Tuple, Union
from unittest.mock import patch, Mock
from parameterized import parameterized
from utils import access_nested_map, get_json, memoize


class TestAccessNestedMap(unittest.TestCase):
    """Test access_nested_map function"""
    @parameterized.expand([
        ({'a': 1}, ('a',), 1),
        ({'a': {'b': 2}}, ('a',), {'b': 2}),
        ({'a': {'b': 2}}, ('a', 'b'), 2)
    ])
    def test_access_nested_map(
            self, nested_map: Dict, path: Tuple, expected: Union[Dict, int]):
        """Test access_nested_map function"""
        self.assertEqual(access_nested_map(nested_map, path), expected)

    def test_access_nested_map_exception(self):
        """Test access_nested_map function with exception"""
        with self.assertRaises(KeyError):
            access_nested_map({'a': 1}, ('a', 'b'))


class TestGetJson(unittest.TestCase):
    """Test get_json function"""
    @parameterized.expand([
        ('http://example.com', {'payload': True}),
        ('http://holberton.io', {'payload': False})
    ])
    @patch('requests.get')
    def test_get_json(self, url: str, payload: Dict, mock_get: Mock):
        """Test get_json function"""
        mock_get.return_value.json.return_value = payload
        self.assertEqual(get_json(url), payload)


class TestMemoize(unittest.TestCase):
    """Test memoize decorator"""

    def test_memoize(self):
        """Test memoize function"""
        class TestClass:
            """Test class"""

            def a_method(self):
                """A method"""
                return 42

            @memoize
            def a_method_memoized(self):
                """A method"""
                return 42

        with patch.object(TestClass, 'a_method', return_value=42) as mock_method:
            tc = TestClass()
            self.assertEqual(tc.a_method(), 42)
            self.assertEqual(tc.a_method(), 42)
            mock_method.assert_called_once()

        with patch.object(TestClass, 'a_method_memoized', return_value=42) as mock_method:
            tc = TestClass()
            self.assertEqual(tc.a_method_memoized(), 42)
            self.assertEqual(tc.a_method_memoized(), 42)
            mock_method.assert_called_once()
