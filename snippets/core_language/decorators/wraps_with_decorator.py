#!/usr/bin/env python3
from functools import wraps


def yes_wraps(f):
    print(f"1. {yes_wraps.__name__}")

    @wraps(f)
    def decorator_impl():
        print(f"2. {yes_wraps.__name__}")
        print(f"3. {bariatric_surgeon.__name__}")
        print(f"4. {decorator_impl.__name__}")
        return f()

    print(f"5. {decorator_impl.__name__}")

    return decorator_impl


@yes_wraps
def bariatric_surgeon():
    """Bariatric surgery specialist."""
    print(f"6. {bariatric_surgeon.__name__}")
    print(f"7. {bariatric_surgeon.__name__}")


if __name__ == '__main__':
    bariatric_surgeon()
    # 1. yes_wraps
    # 5. bariatric_surgeon
    # 2. yes_wraps
    # 3. bariatric_surgeon
    # 4. bariatric_surgeon
    # 6. bariatric_surgeon
    # 7. bariatric_surgeon
