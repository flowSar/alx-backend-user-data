#!/usr/bin/env python3

import logging

logging.basicConfig(filename="logfile.log", level=logging.DEBUG)


def add(x: str, y: str) -> str:
    return x + y

logging.debug(add(8, 5))

#print(add(8, '10'))
