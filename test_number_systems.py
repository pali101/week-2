from number_systems import NumberSystemConverter


class TestNumberSystemConverter:
    def test_bin_to_dec(self):
        assert NumberSystemConverter.bin_to_dec("1011") == 11
        assert NumberSystemConverter.bin_to_dec("0") == 0
        assert NumberSystemConverter.bin_to_dec("1") == 1

        # edge cases
        assert NumberSystemConverter.bin_to_dec("0000") == 0
        assert NumberSystemConverter.bin_to_dec("11111111") == 255

        # Invalid input
        # with pytest.raises(ValueError):
        #     NumberSystemConverter.bin_to_dec("102")

        # with pytest.raises(ValueError):
        #     NumberSystemConverter.bin_to_dec("abc")

    def test_dec_to_bin(self):
        # Standard cases
        assert NumberSystemConverter.dec_to_bin(11) == "1011"
        assert NumberSystemConverter.dec_to_bin(0) == "0"

        # Edge cases
        assert NumberSystemConverter.dec_to_bin(255) == "11111111"
        assert NumberSystemConverter.dec_to_bin(1) == "1"

    def test_dec_to_hex(self):
        # Standard cases
        assert NumberSystemConverter.dec_to_hex(255) == "ff"
        assert NumberSystemConverter.dec_to_hex(0) == "0"
        assert NumberSystemConverter.dec_to_hex(16) == "10"

        # Edge cases
        assert NumberSystemConverter.dec_to_hex(1) == "1"
        assert NumberSystemConverter.dec_to_hex(4095) == "fff"

    def test_hex_to_dec(self):
        # Standard cases
        assert NumberSystemConverter.hex_to_dec("ff") == 255
        assert NumberSystemConverter.hex_to_dec("0") == 0
        assert NumberSystemConverter.hex_to_dec("10") == 16

        # Edge cases
        assert NumberSystemConverter.hex_to_dec("1") == 1
        assert NumberSystemConverter.hex_to_dec("FFF") == 4095
