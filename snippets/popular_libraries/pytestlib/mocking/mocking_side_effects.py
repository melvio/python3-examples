from unittest.mock import Mock

mock = Mock(side_effect=KeyError("NOFAIR"))
try:
    mock()
except KeyError as ex:
    print(ex)  # KeyError: 'NOFAIR'


def other_effect():
    print("Hi mom! No hands.")


mock.side_effect = other_effect

mock()  # Hi mom! No hands.
