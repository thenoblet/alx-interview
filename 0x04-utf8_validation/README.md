

# UTF-8 Validation in Python

This repository provides a Python implementation of a function to validate whether a given data set represents a valid UTF-8 encoding. UTF-8 is a variable-length character encoding used for electronic communication, and this function ensures that a sequence of integers (representing bytes) follows the UTF-8 encoding rules.

## Overview

UTF-8 encoding is widely used due to its ability to represent any character in the Unicode standard while maintaining backward compatibility with ASCII. The function `validUTF8` in this repository checks if a given list of integers represents a valid UTF-8 encoded string. 

### UTF-8 Encoding Rules

1. **1-byte character**: The first bit is `0` (0xxxxxxx).
2. **2-byte character**: The first byte starts with `110` (110xxxxx), and the next byte starts with `10` (10xxxxxx).
3. **3-byte character**: The first byte starts with `1110` (1110xxxx), and the next two bytes start with `10` (10xxxxxx 10xxxxxx).
4. **4-byte character**: The first byte starts with `11110` (11110xxx), and the next three bytes start with `10` (10xxxxxx 10xxxxxx 10xxxxxx).


## Examples

Here are a few examples demonstrating the usage of the `validUTF8` function:

```python
# Example 1: Valid UTF-8 encoding (ASCII character)
data1 = [65]
print(validUTF8(data1))  # Output: True

# Example 2: Valid UTF-8 encoding (sequence of ASCII characters)
data2 = [80, 121, 116, 104, 111, 110, 32, 105, 115, 32, 99, 111, 111, 108, 33]
print(validUTF8(data2))  # Output: True

# Example 3: Invalid UTF-8 encoding
data3 = [229, 65, 127, 256]
print(validUTF8(data3))  # Output: False
```

## How It Works

The `validUTF8` function iterates through each byte in the data list and validates the UTF-8 encoding rules:

1. It first determines the number of bytes in the current character by counting the leading 1s.
2. It then checks if the following bytes (if any) conform to the UTF-8 continuation byte pattern (`10xxxxxx`).
3. If any byte fails to match the expected pattern, the function returns `False`.
4. If all bytes are correctly formatted, the function returns `True`.

### Sample Output

```plaintext
True
True
False
```
