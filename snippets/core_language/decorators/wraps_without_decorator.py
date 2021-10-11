#!/usr/bin/env python3


def no_wraps(f):
    print(f"1. {no_wraps.__name__}")

    def decorator_impl():
        print(f"2. {no_wraps.__name__}")
        print(f"3. {neurologist.__name__}")
        print(f"4. {decorator_impl.__name__}")
        return f()

    print(f"5. {decorator_impl.__name__}")

    return decorator_impl


@no_wraps
def neurologist():
    """Neurology doctor."""
    print(f"6. {neurologist.__name__}")
    print(f"7. {no_wraps.__name__}")


if __name__ == '__main__':
    neurologist()
    # 1. no_wraps
    # 5. decorator_impl
    # 2. no_wraps
    # 3. decorator_impl
    # 4. decorator_impl
    # 6. decorator_impl
    # 7. no_wraps
