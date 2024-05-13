#!/usr/bin/env python3
"""Unittests for client.py"""
import unittest
from typing import Dict
from unittest.mock import (
    MagicMock,
    Mock,
    PropertyMock,
    patch,
)
from parameterized import parameterized, parameterized_class
from requests import HTTPError

from client import (
    GithubOrgClient
)
from fixtures import TEST_PAYLOAD


class TestGithubOrgClient(unittest.TestCase):
    """Test GithubOrgClient class"""

    @parameterized.expand([
        ("google"),
        ("abc"),
    ])
    @patch('client.get_json')
    def test_org(self, org_name: str, mock_get_json: Mock):
        """Test GithubOrgClient.org method"""
        mock_get_json.return_value = TEST_PAYLOAD
        goc = GithubOrgClient(org_name)
        self.assertEqual(goc.org, TEST_PAYLOAD)
        mock_get_json.assert_called_once()

    @patch('client.get_json')
    def test_public_repos_url(self, mock_get_json: Mock):
        """Test GithubOrgClient._public_repos_url method"""
        org_name = 'google'
        goc = GithubOrgClient(org_name)
        goc.org = {'repos_url': 'http://repos.url'}
        self.assertEqual(goc._public_repos_url, 'http://repos.url')
        self.assertIsNone(mock_get_json.assert_called_once())

    @parameterized.expand([
        ("google", {'name': 'repo_1'}),
        ("abc", {'name': 'repo_2'}),
    ])
    @patch('client.GithubOrgClient._public_repos_url', new_callable=PropertyMock)
    @patch('client.get_json')
    def test_public_repos(
            self,
            org_name: str,
            repo_name: Dict,
            mock_get_json: Mock,
            mock_public_repos_url: Mock):
        """Test GithubOrgClient.public_repos method"""
        mock_get_json.return_value = [repo_name]
        goc = GithubOrgClient(org_name)
        self.assertEqual(goc.public_repos(), [repo_name])
        mock_get_json.assert_called_once()
        mock_public_repos_url.assert_called_once()

    @parameterized.expand([
        ("google", {'name': 'repo_1'}),
        ("abc", {'name': 'repo_2'}),
    ])
    @patch('client.GithubOrgClient._public_repos_url', new_callable=PropertyMock)
    @patch('client.get_json')
    def test_public_repos_with_license(
            self,
            org_name: str,
            repo_name: Dict,
            mock_get_json: Mock,
            mock_public_repos_url: Mock):
        """Test GithubOrgClient.public_repos method with license"""
        mock_get_json.return_value = [repo_name]
        goc = GithubOrgClient(org_name)
        self.assertEqual(goc.public_repos(True), [repo_name])
        mock_get_json.assert_called_once()
        mock_public_repos_url.assert_called_once()

    @patch('client.get_json')
    def test_public_repos_url_exception(self, mock_get_json: Mock):
        """Test GithubOrgClient._public_repos_url method with exception"""
        org_name = 'google'
        goc = GithubOrgClient(org_name)
        goc.org = {}
        with self.assertRaises(KeyError):
            goc._public_repos_url
        self.assertIsNone(mock_get_json.assert_not_called())

    @patch('client.get_json')
    def test_public_repos_exception(self, mock_get_json: Mock):
        """Test GithubOrgClient.public_repos method with exception"""
        org_name = 'google'
        goc = GithubOrgClient(org_name)
        goc.org = {'repos_url': 'http://repos.url'}
        mock_get_json.side_effect = HTTPError()
        with self.assertRaises(HTTPError):
            goc.public_repos()
        mock_get_json.assert_called_once()

    @patch('client.get_json')
    def test_public_repos_with_license_exception(self, mock_get_json: Mock):
        """Test GithubOrgClient.public_repos method with license and exception"""
        org_name = 'google'
        goc = GithubOrgClient(org_name)
        goc.org = {'repos_url': 'http://repos.url'}
        mock_get_json.side_effect = HTTPError()
        with self.assertRaises(HTTPError):
            goc.public_repos(True)
        mock_get_json.assert_called_once()
