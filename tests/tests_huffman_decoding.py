import unittest
import sys
from solution.binary_tree import BinaryTree
from solution.huffman_encoding import HuffmanEncoding
from solution.huffman_decoding import HuffmanDecoding



class TestCasesHuffmanDecoding(unittest.TestCase):
    def execute_tests_decode_none_input(self: object) -> None:
        # Arrange
        huffman_decoding_instance: HuffmanDecoding = HuffmanDecoding()

        # Act
        result: str = huffman_decoding_instance.decode(
            "", None)

        # Assert
        self.assertEqual("", result)

    def execute_tests_decode_single_input(self: object) -> None:
        # Arrange
        huffman_encoding_instance: HuffmanEncoding = HuffmanEncoding()
        huffman_decoding_instance: HuffmanDecoding = HuffmanDecoding()
        input_data: str = "A"
        input_data_size: int = sys.getsizeof(input_data)
        encoded_string, binary_tree = huffman_encoding_instance.encode(input_data)

        # Act
        result: str = huffman_decoding_instance.decode(
            encoded_string, binary_tree)
    
    def execute_tests_decode_multiple_input(self: object) -> None:
        # Arrange
        huffman_encoding_instance: HuffmanEncoding = HuffmanEncoding()
        huffman_decoding_instance: HuffmanDecoding = HuffmanDecoding()
        input_data: str = "AAAA ADDD11 11FFAG4D"
        input_data_size: int = sys.getsizeof(input_data)
        encoded_string, binary_tree = huffman_encoding_instance.encode(input_data)

        # Act
        result: str = huffman_decoding_instance.decode(
            encoded_string, binary_tree)

        # Assert
        self.assertEqual(input_data, result)
        self.assertEqual(input_data_size, sys.getsizeof(result))