class NumberSystemConverter:

    @staticmethod
    def bin_to_dec(binary_str: str) -> int:
        """
        Convert a binary string to a decimal integer.
        """
        # Your code here
        pass

    @staticmethod
    def dec_to_bin(decimal: int) -> str:
        """
        Convert a decimal integer to a binary string.
        """
        # Your code here
        pass

    @staticmethod
    def dec_to_hex(decimal: int) -> str:
        """
        Convert a decimal integer to a hexadecimal string.
        """
        # Your code here
        pass

    @staticmethod
    def hex_to_dec(hex_str: str) -> int:
        """
        Convert a hexadecimal string to a decimal integer.
        """
        # Your code here
        pass


if __name__ == "__main__":
    print(NumberSystemConverter.bin_to_dec("1011"))  # Expected output: 11
    print(NumberSystemConverter.dec_to_bin(11))  # Expected output: "1011"
    print(NumberSystemConverter.dec_to_hex(255))  # Expected output: "ff"
    print(NumberSystemConverter.hex_to_dec("ff"))  # Expected output: 255
