from tests.tests_huffman_decoding import TestCasesHuffmanDecoding
from tests.tests_huffman_encoding import TestCasesHuffmanEncoding
import sys
from solution.huffman_encoding import HuffmanEncoding
from solution.huffman_decoding import HuffmanDecoding

if __name__ == "__main__":
    ###################################
    # Tests
    ###################################
    tests_huffman_encoding: TestCasesHuffmanEncoding = TestCasesHuffmanEncoding()

    tests_huffman_encoding.execute_tests_create_priority_queue_empty_string()
    tests_huffman_encoding.execute_tests_create_priority_queue_none_string()
    tests_huffman_encoding.execute_tests_create_priority_queue_single_character()
    tests_huffman_encoding.execute_tests_create_priority_queue_multiple_characters()

    tests_huffman_encoding.execute_tests_create_binary_tree_empty_queue()
    tests_huffman_encoding.execute_tests_create_binary_tree_single_item_in_queue()
    tests_huffman_encoding.execute_tests_create_binary_tree_two_items_in_queue()
    tests_huffman_encoding.execute_tests_create_binary_tree_multiple_items_in_queue()

    tests_huffman_encoding.execute_tests_create_binary_for_character_empty_input_data()
    tests_huffman_encoding.execute_tests_create_binary_for_character_single_input_data()
    tests_huffman_encoding.execute_tests_create_binary_for_character_two_input_data()
    tests_huffman_encoding.execute_tests_create_binary_for_character_three_input_data()
    tests_huffman_encoding.execute_tests_create_binary_for_character_multiple_input_data()
    tests_huffman_encoding.execute_tests_encode_input_data_none()
    tests_huffman_encoding.execute_tests_encode_input_data_empty_string()
    tests_huffman_encoding.execute_tests_encode_input_data_single_character()
    tests_huffman_encoding.execute_tests_encode_input_data_multiple_character()

    tests_huffman_decoding: TestCasesHuffmanDecoding = TestCasesHuffmanDecoding()

    tests_huffman_decoding.execute_tests_decode_none_input()
    tests_huffman_decoding.execute_tests_decode_single_input()
    tests_huffman_decoding.execute_tests_decode_multiple_input()

    ###################################
    # Demo
    ###################################
    huffman_encoding_instance: HuffmanEncoding = HuffmanEncoding()
    huffman_decoding_instance: HuffmanDecoding = HuffmanDecoding()

    a_great_sentence = "The bird is the word"

    print("The size of the data is: {}\n".format(
        sys.getsizeof(a_great_sentence)))
    print("The content of the data is: {}\n".format(a_great_sentence))

    encoded_data, tree = huffman_encoding_instance.encode(a_great_sentence)

    print("The size of the encoded data is: {}\n".format(
        sys.getsizeof(int(encoded_data, base=2))))
    print("The content of the encoded data is: {}\n".format(encoded_data))

    decoded_data = huffman_decoding_instance.decode(encoded_data, tree)

    print("The size of the decoded data is: {}\n".format(
        sys.getsizeof(decoded_data)))
    print("The content of the encoded data is: {}\n".format(decoded_data))

    """
    Output:
    
    The size of the data is: 69

    The content of the data is: The bird is the word

    The size of the encoded data is: 36

    The content of the encoded data is: 1110000100011011101010100111111001001111101010001000110101101101001111

    The size of the decoded data is: 69

    The content of the encoded data is: The bird is the word
    """
