#!/usr/bin/env python3

from unittest.mock import MagicMock


class ProductionClass:
    def method(self):
        pass


thing = ProductionClass()
thing.method = MagicMock(return_value=42)

print(thing.method(3, 4, 5, key="value"))  # 42

thing.method.assert_called_once()  # returns None if successful
thing.method.assert_called_with(3, 4, 5, key="value")  # returns None if successful

try:
    print(thing.method.assert_not_called())
except AssertionError as ex:
    print(ex)
    # Expected 'mock' to not have been called. Called 1 times.
    # Calls: [call(3, 4, 5, key='value')].
