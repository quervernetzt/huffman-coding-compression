from solution.binary_tree import BinaryTree
import unittest
from solution.huffman_encoding import HuffmanEncoding
from heapq import heappop


class TestCasesHuffmanEncoding(unittest.TestCase):
    def execute_tests_create_priority_queue_empty_string(self: object) -> None:
        # Arrange
        huffman_encoding_instance: HuffmanEncoding = HuffmanEncoding()
        input_data: str = ""

        # Act
        result: list = huffman_encoding_instance.create_priority_queue(
            input_data)

        # Assert
        self.assertListEqual([], result)

    def execute_tests_create_priority_queue_none_string(self: object) -> None:
        # Arrange
        huffman_encoding_instance: HuffmanEncoding = HuffmanEncoding()
        input_data: str = None

        # Act
        result: list = huffman_encoding_instance.create_priority_queue(
            input_data)

        # Assert
        self.assertListEqual([], result)

    def execute_tests_create_priority_queue_single_character(self: object) -> None:
        # Arrange
        huffman_encoding_instance: HuffmanEncoding = HuffmanEncoding()
        input_data: str = "A"

        # Act
        result: list = huffman_encoding_instance.create_priority_queue(
            input_data)

        # Assert
        result_element: tuple = heappop(result)
        self.assertEqual(1, result_element[0])
        self.assertEqual("A", result_element[1])
        self.assertEqual("A", result_element[2].value)

    def execute_tests_create_priority_queue_multiple_characters(self: object) -> None:
        # Arrange
        huffman_encoding_instance: HuffmanEncoding = HuffmanEncoding()
        input_data: str = "AAAAA DDD111 1FFAG4D"

        # Act
        result: list = huffman_encoding_instance.create_priority_queue(
            input_data)

        # Assert
        result_element: tuple = heappop(result)
        self.assertEqual(1, result_element[0])
        self.assertEqual("4", result_element[1])
        self.assertEqual("4", result_element[2].value)

        result_element = heappop(result)
        self.assertEqual(1, result_element[0])
        self.assertEqual("G", result_element[1])
        self.assertEqual("G", result_element[2].value)

        result_element = heappop(result)
        self.assertEqual(2, result_element[0])
        self.assertEqual(" ", result_element[1])
        self.assertEqual(" ", result_element[2].value)

        result_element = heappop(result)
        self.assertEqual(2, result_element[0])
        self.assertEqual("F", result_element[1])
        self.assertEqual("F", result_element[2].value)

        result_element = heappop(result)
        self.assertEqual(4, result_element[0])
        self.assertEqual("1", result_element[1])
        self.assertEqual("1", result_element[2].value)

        result_element = heappop(result)
        self.assertEqual(4, result_element[0])
        self.assertEqual("D", result_element[1])
        self.assertEqual("D", result_element[2].value)

        result_element = heappop(result)
        self.assertEqual(6, result_element[0])
        self.assertEqual("A", result_element[1])
        self.assertEqual("A", result_element[2].value)

    def execute_tests_create_binary_tree_empty_queue(self: object) -> None:
        # Arrange
        huffman_encoding_instance: HuffmanEncoding = HuffmanEncoding()
        input_data: str = ""
        min_heap_queue: list = huffman_encoding_instance.create_priority_queue(
            input_data)

        # Act
        result: BinaryTree = huffman_encoding_instance.create_binary_tree(
            min_heap_queue)

        # Assert
        self.assertIsNone(result)

    def execute_tests_create_binary_tree_single_item_in_queue(self: object) -> None:
        # Arrange
        huffman_encoding_instance: HuffmanEncoding = HuffmanEncoding()
        input_data: str = "A"
        min_heap_queue: list = huffman_encoding_instance.create_priority_queue(
            input_data)

        # Act
        result: BinaryTree = huffman_encoding_instance.create_binary_tree(
            min_heap_queue)

        # Assert
        result_list: list = result.tree_to_list()
        self.assertEqual(1, len(result_list))
        self.assertEqual(["A"], result_list)

    def execute_tests_create_binary_tree_two_items_in_queue(self: object) -> None:
        # Arrange
        huffman_encoding_instance: HuffmanEncoding = HuffmanEncoding()
        input_data: str = "BAABB"
        min_heap_queue: list = huffman_encoding_instance.create_priority_queue(
            input_data)

        # Act
        result: BinaryTree = huffman_encoding_instance.create_binary_tree(
            min_heap_queue)

        # Assert
        result_list: list = result.tree_to_list()
        self.assertEqual(3, len(result_list))
        self.assertListEqual([5, "A", "B"], result_list)

    def execute_tests_create_binary_tree_multiple_items_in_queue(self: object) -> None:
        # Arrange
        huffman_encoding_instance: HuffmanEncoding = HuffmanEncoding()
        input_data: str = "AAAA ADDD11 11FFAG4D"
        min_heap_queue: list = huffman_encoding_instance.create_priority_queue(
            input_data)

        # Act
        result: BinaryTree = huffman_encoding_instance.create_binary_tree(
            min_heap_queue)

        # Assert
        result_list: list = result.tree_to_list()
        self.assertEqual(13, len(result_list))
        self.assertListEqual(
            [20, 8, "1", "D", 12, "A", 6, "F", 4, " ", 2, "4", "G"], result_list)

    def execute_tests_create_binary_for_character_empty_input_data(self: object) -> None:
        # Arrange
        huffman_encoding_instance: HuffmanEncoding = HuffmanEncoding()
        input_data: str = ""
        min_heap_queue: list = huffman_encoding_instance.create_priority_queue(
            input_data)
        binary_tree: BinaryTree = huffman_encoding_instance.create_binary_tree(
            min_heap_queue)

        # Act
        result: str = huffman_encoding_instance.encode_input_data(
            input_data, binary_tree)

        # Assert
        self.assertEqual("", result)

    def execute_tests_create_binary_for_character_single_input_data(self: object) -> None:
        # Arrange
        huffman_encoding_instance: HuffmanEncoding = HuffmanEncoding()
        input_data: str = "A"
        min_heap_queue: list = huffman_encoding_instance.create_priority_queue(
            input_data)
        binary_tree: BinaryTree = huffman_encoding_instance.create_binary_tree(
            min_heap_queue)

        # Act
        result: str = huffman_encoding_instance.encode_input_data(
            input_data, binary_tree)

        # Assert
        self.assertEqual("2", result)

    def execute_tests_create_binary_for_character_two_input_data(self: object) -> None:
        # Arrange
        huffman_encoding_instance: HuffmanEncoding = HuffmanEncoding()
        input_data: str = "AB"
        min_heap_queue: list = huffman_encoding_instance.create_priority_queue(
            input_data)
        binary_tree: BinaryTree = huffman_encoding_instance.create_binary_tree(
            min_heap_queue)

        # Act
        result: str = huffman_encoding_instance.encode_input_data(
            input_data, binary_tree)

        # Assert
        self.assertEqual("01", result)

    def execute_tests_create_binary_for_character_three_input_data(self: object) -> None:
        # Arrange
        huffman_encoding_instance: HuffmanEncoding = HuffmanEncoding()
        input_data: str = "ABC"
        min_heap_queue: list = huffman_encoding_instance.create_priority_queue(
            input_data)
        binary_tree: BinaryTree = huffman_encoding_instance.create_binary_tree(
            min_heap_queue)

        # Act
        result: str = huffman_encoding_instance.encode_input_data(
            input_data, binary_tree)

        # Assert
        self.assertEqual("10110", result)

    def execute_tests_create_binary_for_character_multiple_input_data(self: object) -> None:
        # Arrange
        huffman_encoding_instance: HuffmanEncoding = HuffmanEncoding()
        input_data: str = "AAAA ADDD11 11FFAG4D"
        min_heap_queue: list = huffman_encoding_instance.create_priority_queue(
            input_data)
        binary_tree: BinaryTree = huffman_encoding_instance.create_binary_tree(
            min_heap_queue)

        # Act
        result: str = huffman_encoding_instance.encode_input_data(
            input_data, binary_tree)

        # Assert
        self.assertEqual(
            "1010101011101001010100001110000011011010111111111001", result)

    def execute_tests_encode_input_data_none(self: object) -> None:
        # Arrange
        huffman_encoding_instance: HuffmanEncoding = HuffmanEncoding()
        input_data: object = None

        # Act
        result: object = huffman_encoding_instance.encode(input_data)

        # Assert
        self.assertIsNone(result)

    def execute_tests_encode_input_data_empty_string(self: object) -> None:
        # Arrange
        huffman_encoding_instance: HuffmanEncoding = HuffmanEncoding()
        input_data: object = ""

        # Act
        result: object = huffman_encoding_instance.encode(input_data)

        # Assert
        self.assertIsNone(result)

    def execute_tests_encode_input_data_single_character(self: object) -> None:
        # Arrange
        huffman_encoding_instance: HuffmanEncoding = HuffmanEncoding()
        input_data: object = "A"

        # Act
        binary_respresentation, binary_tree = huffman_encoding_instance.encode(
            input_data)

        # Assert
        self.assertEqual("2", binary_respresentation)
        self.assertEqual("A", binary_tree.get_root().value)

    def execute_tests_encode_input_data_multiple_character(self: object) -> None:
        # Arrange
        huffman_encoding_instance: HuffmanEncoding = HuffmanEncoding()
        input_data: object = "AAAA ADDD11 11FFAG4D"

        # Act
        binary_respresentation, binary_tree = huffman_encoding_instance.encode(
            input_data)

        # Assert
        self.assertEqual(
            "1010101011101001010100001110000011011010111111111001", binary_respresentation)
        self.assertEqual(20, binary_tree.get_root().value)
