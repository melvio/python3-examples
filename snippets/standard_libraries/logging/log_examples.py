#!/usr/bin/env python3
import logging

def setup_logging() -> logging.Logger:
    logging.basicConfig(
        # [DEBUG][hopla.py] 2021-08-19T18:28:13 - Something here
        format='[%(levelname)s][%(filename)s] %(asctime)s - %(message)s',
        level=logging.DEBUG,
        datefmt="%Y-%m-%dT%H:%M:%S"
    )
    return logging.getLogger(__name__)


log = setup_logging()
log.debug("Something here")
