#!/usr/bin/env python3
import datetime

from typing import Callable


def print_now(function) -> Callable[[int, int], int]:
    def wrapper_impl(x, y):
        print(datetime.datetime.now())
        return function(x, y)

    return wrapper_impl


def calculate_sum1(x: int, y: int) -> int:
    return x + y


@print_now
def calculate_sum2(x: int, y: int) -> int:
    return x + y


@print_now  # doesn't work, because @print_now only works for functions with 2 args
def twice1(x: int) -> int:
    return x * 2


def generic_print_now(function) -> Callable:
    def wrapper_impl(*args, **kwargs):
        print(datetime.datetime.now())
        return function(*args, **kwargs)

    return wrapper_impl


@generic_print_now  # does work, because this decorator accepts any amount of argument
def twice2(x: int) -> int:
    return x * 2


if __name__ == '__main__':
    sum_1 = calculate_sum1(1, 2)
    print(f"{sum_1=}")
    sum_2 = calculate_sum2(1, 2)
    print(f"{sum_2=}")

    # twice_1 = twice1(3)
    # print(f"{twice_1=}")

    twice_2 = twice2(3)
    print(f"{twice_2=}")

