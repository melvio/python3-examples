#!/usr/bin/env python3
from typing import Union, Optional

print(Union[int, str] == Union[str, int, int])  # True

print(Optional[int] == Union[int, None])  # True
