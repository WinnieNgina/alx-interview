#!/usr/bin/python3
"""
script that reads stdin line by line and computes metrics
"""
import sys
import signal

# Initialize variables
status_codes = [200, 301, 400, 401, 403, 404, 405, 500]
status_dict = dict.fromkeys(status_codes, 0)
total_size = 0
line_count = 0


# Function to print statistics
def print_stats():
    print("File size: {}".format(total_size))
    for code in sorted(status_dict):
        if status_dict[code] > 0:
            print("{}: {}".format(code, status_dict[code]))


# Function to handle keyboard interruption
def signal_handler(sig, frame):
    print_stats()
    sys.exit(0)


# Set signal handler
signal.signal(signal.SIGINT, signal_handler)

try:
    for line in sys.stdin:
        try:
            parts = line.split()
            size = int(parts[-1])
            status = int(parts[-2])
            total_size += size
            if status in status_codes:
                status_dict[status] += 1
        except (IndexError, ValueError):
            continue

        line_count += 1
        if line_count % 10 == 0:
            print_stats()

except KeyboardInterrupt:
    pass

finally:
    print_stats()
