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
    def test_public_repos_url(self) -> None:
        """Tests the `_public_repos_url` property."""
        with patch(
                "client.GithubOrgClient.org",
                new_callable=PropertyMock,
                ) as mock_org:
            mock_org.return_value = {
                'repos_url': "https://api.github.com/users/google/repos",
            }
            self.assertEqual(
                GithubOrgClient("google")._public_repos_url,
                "https://api.github.com/users/google/repos",
            )

    @parameterized.expand([
        ("google", {'name': 'repo_1'}),
        ("abc", {'name': 'repo_2'}),
    ])
    @patch('client.GithubOrgClient._public_repos_url',
           new_callable=PropertyMock)

    @patch('client.get_json')
    def test_public_repos(self, mock_get_json: MagicMock) -> None:
        """Tests the `public_repos` method."""
        test_payload = {
            'repos_url': "https://api.github.com/users/google/repos",
            'repos': [
                {
                    "id": 7697149,
                    "name": "episodes.dart",
                    "private": False,
                    "owner": {
                        "login": "google",
                        "id": 1342004,
                    },
                    "fork": False,
                    "url": "https://api.github.com/repos/google/episodes.dart",
                    "created_at": "2013-01-19T00:31:37Z",
                    "updated_at": "2019-09-23T11:53:58Z",
                    "has_issues": True,
                    "forks": 22,
                    "default_branch": "master",
                },
                {
                    "id": 8566972,
                    "name": "kratu",
                    "private": False,
                    "owner": {
                        "login": "google",
                        "id": 1342004,
                    },
                    "fork": False,
                    "url": "https://api.github.com/repos/google/kratu",
                    "created_at": "2013-03-04T22:52:33Z",
                    "updated_at": "2019-11-15T22:22:16Z",
                    "has_issues": True,
                    "forks": 32,
                    "default_branch": "master",
                },
            ]
        }
        mock_get_json.return_value = test_payload["repos"]
        with patch(
                "client.GithubOrgClient._public_repos_url",
                new_callable=PropertyMock,
                ) as mock_public_repos_url:
            mock_public_repos_url.return_value = test_payload["repos_url"]
            self.assertEqual(
                GithubOrgClient("google").public_repos(),
                [
                    "episodes.dart",
                    "kratu",
                ],
            )
            mock_public_repos_url.assert_called_once()
        mock_get_json.assert_called_once()

    @parameterized.expand([
        ({'license': {'key': "bsd-3-clause"}}, "bsd-3-clause", True),
        ({'license': {'key': "bsl-1.0"}}, "bsd-3-clause", False),
    ])
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
        """Test GithubOrgClient.public_repos method
        with license and exception"""
        org_name = 'google'
        goc = GithubOrgClient(org_name)
        goc.org = {'repos_url': 'http://repos.url'}
        mock_get_json.side_effect = HTTPError()
        with self.assertRaises(HTTPError):
            goc.public_repos(True)
        mock_get_json.assert_called_once()
