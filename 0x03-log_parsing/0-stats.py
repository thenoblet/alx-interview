#!/usr/bin/python3

"""
Log Parsing Script

This module processes log entries from standard input, focusing on specific
HTTP status codes and file sizes.
It tracks the total size of files transferred and the frequency of specific
HTTP status codes (e.g., 200, 301, 400).
The script outputs the total file size and the count of each relevant HTTP
status code after every 10 log entries.
If interrupted by a SIGINT (e.g., Ctrl+C), it prints the accumulated
data before exiting.
"""

import sys
import re


def print_stats(status_codes: dict, total_file_size: int) -> None:
    """
    Prints the total file size and the count of each status code tracked.
    """
    print(f"File size: {total_file_size}")
    for status_code, value in status_codes.items():
        if value > 0:
            print(f"{status_code}: {value}")


def update_stats(
        status_codes: dict,
        status_code: int,
        file_size: int,
        total_file_size: int
) -> int:
    """
    Updates the total file size and the count of a specific status code.

    Args:
        status_code (int): The HTTP status code to track.
        file_size (int): The size of the file transferred.
    """
    total_file_size += file_size

    if status_code in status_codes:
        status_codes[status_code] += 1

    return total_file_size


def parse_log() -> None:
    """
    Parses log entries from standard input, tracking the total file size and
    counting occurrences of specific HTTP status codes. After every 10 lines,
    it prints the current total file size and status code counts.

    The log format expected is as follows:
    <IP> - [<date>] "GET /projects/260 HTTP/1.1" <status code> <file size>

    """
    status_codes = {
        200: 0,
        301: 0,
        400: 0,
        401: 0,
        403: 0,
        404: 0,
        405: 0,
        500: 0
    }

    log_pattern = re.compile(
        r'(\d{1,3}\.){3}\d{1,3} - \['
        r'\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}\.\d{6}\] '
        r'"GET /projects/260 HTTP/1.1" '
        r'\d{3} \d+'
    )

    line_count = 0
    total_file_size = 0

    try:
        for line in sys.stdin:
            match = log_pattern.match(line)
            if not match:
                continue

            log_parts = line.strip().split()

            file_size = int(log_parts[-1])
            status_code = int(log_parts[-2])
            total_file_size = update_stats(
                status_codes, status_code, file_size, total_file_size
            )

            line_count += 1
            if line_count == 10:
                print_stats(status_codes, total_file_size)
                line_count = 0
    except KeyboardInterrupt:
        print_stats(status_codes, total_file_size)
        sys.exit(0)

    if line_count > 0:
        print_stats(status_codes, total_file_size)


if __name__ == "__main__":
    parse_log()
