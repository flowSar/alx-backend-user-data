#!/usr/bin/env python3
""" module """
import re
from typing import List
import logging


def filter_datum(fields: List[str],
                 redaction: str,
                 message: str,
                 separator: str) -> str:
    """Obfuscates specified fields in a log message."""
    pattern = f"({'|'.join(fields)})=([^ {separator}]+)"
    return re.sub(pattern, f"\\1={redaction}", message)


class RedactingFormatter(logging.Formatter):
    """ Redacting Formatter class
        """

    REDACTION = "***"
    FORMAT = "[HOLBERTON] %(name)s %(levelname)s %(asctime)-15s: %(message)s"
    SEPARATOR = ";"

    def __init__(self, fields: List[str]):
        """initialize attribute"""
        super(RedactingFormatter, self).__init__(self.FORMAT)
        self.fields = fields

    def format(self, record: logging.LogRecord) -> str:
        """ format method"""
        return filter_datum(self.fields,
                            RedactingFormatter.REDACTION,
                            message, RedactingFormatter.SEPARATOR)
