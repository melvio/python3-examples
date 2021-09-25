#!/usr/bin/env python3
from unittest.mock import MagicMock, patch
from mypack import mycode


class TestGoodResponse:
    @patch("mypack.mycode.requests.get")
    def test_returns_true_on_200(self, mock: MagicMock):
        url = 'https://example.com'

        mock.return_value.status_code = 200
        mock.return_value.json = lambda: {"Status": "I'm Awake"}

        result = mycode.good_response(url)

        assert result

        mock.assert_called_with(url)

    @patch("mypack.mycode.requests.get")
    def test_returns_false_on_404(self, mock: MagicMock):
        url = "https://google.io/unavailable"

        mock.return_value.status_code = 404
        mock.return_value.json = lambda: {"Status": "I'm Busy"}

        result = mycode.good_response(url)

        assert result is False

        mock.assert_called_with(url)


