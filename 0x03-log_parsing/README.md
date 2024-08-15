Here's a detailed `README.md` file for your log parsing project:

```markdown
# Log Parsing Project

This project consists of two Python scripts designed to generate and parse log data. The `0-generator.py` script generates random log entries, and the `0-stats.py` script processes these logs to compute various metrics. 

## Overview

- **`0-generator.py`**: Generates random log data in a specified format.
- **`0-stats.py`**: Reads log data from standard input, computes statistics, and prints them periodically.

## Input Format

The log lines should adhere to the following format:

```
<IP Address> - [<date>] "GET /projects/260 HTTP/1.1" <status code> <file size>
```

**Example:**
```
192.168.1.1 - [2024-08-15] "GET /projects/260 HTTP/1.1" 200 1234
```

## Features

- **Metrics Calculation**: Computes the total file size and counts the occurrences of specific HTTP status codes.
- **Periodic Output**: Outputs statistics after every 10 lines or upon keyboard interruption.
- **Graceful Interruption Handling**: Outputs accumulated statistics if interrupted (e.g., CTRL + C).

## Usage

1. **Generate Log Data:**

   Run `0-generator.py` to generate log data. You can control the number of lines and the randomness of the data.

   ```sh
   ./0-generator.py
   ```

2. **Process Log Data:**

   Pipe the output of `0-generator.py` into `0-stats.py` to compute and print statistics.

   ```sh
   ./0-generator.py | ./0-stats.py
   ```

## Example

Run the following command to generate log data and compute statistics:

```sh
./0-generator.py | ./0-stats.py
```

**Sample Output:**

```
File size: 5213
200: 2
401: 1
403: 2
404: 1
405: 1
500: 3
File size: 11320
200: 3
301: 2
400: 1
401: 2
403: 3
404: 4
405: 2
500: 3
File size: 16305
200: 3
301: 3
400: 4
401: 2
403: 5
404: 5
405: 4
500: 4
^C
File size: 17146
200: 4
301: 3
400: 4
401: 2
403: 6
404: 6
405: 4
500: 4
```

## Script Details

- **`0-generator.py`**: Generates random log entries with a random delay between each entry. The generated logs include IP addresses, timestamps, status codes, and file sizes.

- **`0-stats.py`**: Reads log lines from stdin, parses them, and prints the total file size and counts of specific status codes. Statistics are printed every 10 lines and upon interruption.

## Handling Interruptions

If you interrupt the script with CTRL + C, it will print the statistics collected up to that point.
