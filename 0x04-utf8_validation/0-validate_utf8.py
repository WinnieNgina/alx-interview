#!/usr/bin/python3
"""UTF-8 Validation"""


def validUTF8(data):
    """Checks for UTF-8 encoding"""
    i = 0
    while i < len(data):
        num_bytes = data[i] >> 4
        if num_bytes == 0:
            i += 1
        elif num_bytes == 15:
            return False
        else:
            i += num_bytes
    return True
