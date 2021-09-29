import unittest

from caesar_cipher import encode_caesar_cipher, decode_caesar_cipher


class TestCaesarCipher(unittest.TestCase):
    def test_encode_lower_case(self):
        """
        Test that all the lower cased characters are ciphered correctly
        """
        self.assertEqual(encode_caesar_cipher('abcdefghijklmnopqrstuvwxyz'), "defghijklmnopqrstuvwxyzabc")

    def test_encode_upper_case(self):
        """
        Test that all the upper cased characters are converted to lower cased characters and  ciphered correctly
        """
        self.assertEqual(encode_caesar_cipher("ABCDEFGHIJKLMNOPQRSTUVWXYZ"), "defghijklmnopqrstuvwxyzabc")

    def test_encode_spaces(self):
        """
        Test that spaces are ignored when ciphering
        """
        self.assertEqual(encode_caesar_cipher("Hello World"), 'khoor zruog')

    def test_encode_ignore_spaces(self):
        """
        Test that if ignore_spaces is set to true the spaces are indeed ignored
        """
        self.assertEqual(encode_caesar_cipher("Hello World", ignore_spaces=True), 'khoorzruog')

    def test_encode_general_key(self):
        """
        Test that specifying a specific key works
        """
        self.assertEqual(encode_caesar_cipher("Hello World", 0), 'hello world')
        self.assertEqual(encode_caesar_cipher("Hello World", 26), 'hello world')
        self.assertEqual(encode_caesar_cipher("Hello World", 25), 'gdkkn vnqkc')
        self.assertEqual(encode_caesar_cipher("The quick brown fox jumps over the lazy dog", 42), 'jxu gkysa rhemd ven zkcfi eluh jxu bqpo tew')

    def test_decode_lower_case(self):
        """
        Test that all the lower cased characters are ciphered correctly
        """
        self.assertEqual(decode_caesar_cipher("defghijklmnopqrstuvwxyzabc"), "abcdefghijklmnopqrstuvwxyz")

    def test_decode_upper_case(self):
        """
        Test that all the upper cased characters are converted to lower cased characters and  ciphered correctly
        """
        self.assertEqual(decode_caesar_cipher("DEFGHIJKLMNOPQRSTUVWXYZABC"), "abcdefghijklmnopqrstuvwxyz")

    def test_decode_spaces(self):
        """
        Test that spaces are ignored when ciphering
        """
        self.assertEqual(decode_caesar_cipher("Khoor Zruog"), "hello world")

    def test_decode_general_key(self):
        """
        Test that specifying a specific key works
        """
        self.assertEqual(decode_caesar_cipher("Hello World", 0), 'hello world')
        self.assertEqual(decode_caesar_cipher("Hello World", 26), 'hello world')
        self.assertEqual(decode_caesar_cipher("gdkkn vnqkc", 25), 'hello world')
        self.assertEqual(decode_caesar_cipher("jxu gkysa rhemd ven zkcfi eluh jxu bqpo tew", 42), 'the quick brown fox jumps over the lazy dog')

