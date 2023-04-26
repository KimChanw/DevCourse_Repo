import unittest
from to_hex import convert_decimal_to_hex

class test_decimal_to_hex(unittest.TestCase):
    def test_single_digit_number(self):
        self.assertEqual(convert_decimal_to_hex(0), '0')
        self.assertEqual(convert_decimal_to_hex(1), '1')
        self.assertEqual(convert_decimal_to_hex(5), '5')

    def test_single_digit_number(self):
        self.assertEqual(convert_decimal_to_hex(10), 'A')
        self.assertEqual(convert_decimal_to_hex(15), 'F')
        self.assertEqual(convert_decimal_to_hex(16), '10')

    def test_large_number(self):
        self.assertEqual(convert_decimal_to_hex(4096), '1000')
        self.assertEqual(convert_decimal_to_hex(65535), 'FFFF')

    # 음수에 대해 테스트
    def test_neg_number(self):
        self.assertEqual(convert_decimal_to_hex(-1), '-1')
        self.assertEqual(convert_decimal_to_hex(-10), '-A')

if __name__ == '__main__':
    unittest.main()
