#!/usr/bin/env python3
from dataclasses import dataclass
from unittest.mock import patch, MagicMock

from mypack.mycode2 import get_content


@dataclass
class MockOkResponse:
    status_code: int
    content = "Hiyaa!"


class TestMyCode2:
    @patch("mypack.mycode2.get")
    def test_get_content_ok(self, mock: MagicMock):
        url = "https://google.io/unavailable"

        mock.return_value = MockOkResponse(status_code=200)

        content_result = get_content(url)

        assert content_result == "Hiyaa!"
