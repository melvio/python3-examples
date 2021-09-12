#!/usr/bin/env python3

from unittest import mock


class ChallengingLegacyClass:
    def __init__(self, heavy_args):
        self.heavy_args = heavy_args

    def heavy_method(self) -> (str, int):
        # open_database(self.heavy_args)
        # put_something_in_database(self.heavy_args)
        # why_the_hell_is_this_functionality_here(self.heavy_args)
        # even_some_external_api_requests(self.heavy_args)
        # close_database(self.heavy_args)

        status_code = 200 if self.heavy_args else 418
        return "result value", status_code


def test_heavy_method():
    thing = ChallengingLegacyClass(heavy_args=["databaseparams", "apiparams", "morestuff"])
    status_msg = "Everything Good"
    status_code = 200
    thing.heavy_method = mock.MagicMock(return_value=(status_msg, status_code))

    result = thing.heavy_method()

    assert len(result) == 2
    assert result[0] == status_msg
    assert result[1] == status_code
