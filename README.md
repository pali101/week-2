# Week 2 Assignment: Number System Converter

Implement methods to convert between binary, decimal, and hexadecimal systems in the `NumberSystemConverter` class.

### Methods

1. **bin_to_dec(binary_str: str) -> int**: Convert binary string to decimal.
2. **dec_to_bin(decimal: int) -> str**: Convert decimal integer to binary string.
3. **dec_to_hex(decimal: int) -> str**: Convert decimal integer to hexadecimal string.
4. **hex_to_dec(hex_str: str) -> int**: Convert hexadecimal string to decimal.

### Example

```python
print(NumberSystemConverter.bin_to_dec("1011"))  # Output: 11
print(NumberSystemConverter.dec_to_bin(11))      # Output: "1011"
print(NumberSystemConverter.dec_to_hex(255))     # Output: "ff"
print(NumberSystemConverter.hex_to_dec("ff"))    # Output: 255
