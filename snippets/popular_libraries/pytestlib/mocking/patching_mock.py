#!/usr/bin/env python3

import requests
from unittest import mock

CALL_TIMES = 3

URL = "https://api.github.com/zen"


def get_github_data() -> set:
    s = set()
    for _ in range(CALL_TIMES):
        text_response = requests.get(URL).text
        s.add(text_response)

    return s


def mocked_requests_get(mock_url: str):
    class MockResponse:
        def __init__(self, text, status_code):
            self.text = text
            self.status_code = status_code

    if mock_url == URL:
        return MockResponse(text="test_text", status_code=200)


@mock.patch("requests.get", side_effect=mocked_requests_get)
def test_get_github_data(mock_get: mock.MagicMock):
    """patch mock with a function annotation"""
    result = get_github_data()
    assert result == {"test_text"}
    assert len(mock_get.call_args_list) == CALL_TIMES
    mock_get.assert_called()


def test_get_github_data2():
    """Patch mock with a context manager"""
    with mock.patch("requests.get", side_effect=mocked_requests_get) as mock_get:
        result = get_github_data()
        assert result == {"test_text"}
        assert len(mock_get.call_args_list) == CALL_TIMES
