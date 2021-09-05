#!/usr/bin/env python3

#!/usr/bin/env python3
import logging

log = logging.getLogger(name="ZebraLogger")

try:
    raise TypeError("horse") from BaseException("Didn't expect this")
except TypeError as ex:
    log.warning(ex)
    # horse

    log.warning(str(ex))
    # horse

    log.warning(ex, exc_info=ex)  # horse
    # horse
    # BaseException: Didn't expect this
    #
    # The above exception was the direct cause of the following exception:
    #
    # Traceback (most recent call last):
    #     File "how_to_log_exceptions.py", line 9, in <module>
    #         raise TypeError("horse")
    # TypeError: horse
