#!/usr/bin/python3
"""Log parsing"""
import sys
import re

total_file_size = 0
status_code_counts = {200: 0, 301: 0, 400: 0, 401: 0, 403: 0, 404: 0, 405: 0, 500: 0}
log_entry_pattern = re.compile(r'(\d+\.\d+\.\d+\.\d+) - \[.*\] "GET /projects/260 HTTP/1.1" (\d+) (\d+)')

try:
    for i, line in enumerate(sys.stdin):
        match = log_entry_pattern.match(line)
        if match:
            file_size = int(match.group(3))
            status_code = int(match.group(2))
            total_file_size += file_size
            if status_code in status_code_counts:
                status_code_counts[status_code] += 1

        if (i + 1) % 10 == 0 or i == 0:
            print(f'Total file size: {total_file_size}')
            for status_code, count in sorted(status_code_counts.items()):
                if count > 0:
                    print(f'{status_code}: {count}')

except KeyboardInterrupt:
    print(f'Total file size: {total_file_size}')
    for status_code, count in sorted(status_code_counts.items()):
        if count > 0:
            print(f'{status_code}: {count}')
