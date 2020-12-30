from collections import Counter
from typing import Union, Tuple
from heapq import heapify, heappush, heappop
from solution.binary_tree import BinaryTree, BinaryTreeNode


class HuffmanEncoding(object):
    def __init__(self: object) -> None:
        """
        Constructor.
        """
        pass

    def encode(self: object, input_data: object) -> Union[Tuple[str, BinaryTree], None]:
        """
        Constructor.

        Parameters
        ----------
        input_data: object, required 
            The input data to be encoded.

        Returns
        ----------
        Union[(str, BinaryTree), None]
            Returns a tuple of the binary sequence and the corresponding binary tree or None.
        """

        if not input_data:
            #print("Input object is empty...")
            return
        else:
            input_data_str: str = str(input_data)

            min_heap_priority_queue: list = self.create_priority_queue(
                input_data_str)

            binary_tree: BinaryTree = self.create_binary_tree(
                min_heap_priority_queue)
            #print("Created binary tree...")

            if binary_tree:
                binary_representation: str = self.encode_input_data(
                    input_data_str, binary_tree)
                #print("Created binary representation...")
                return binary_representation, binary_tree
            else:
                return

    def create_priority_queue(self: object, input_data: str) -> list:
        """
        Creates a priority queue out of each distinct character ordered by the frequency each character occurs within the input string.
        The order is from lowest to highest. Each element in the queue is a binary tree node.

        Parameters
        ----------
        input_data: str, required 
            The input string to be encoded.

        Returns
        ----------
        list
            Returns the priority queue as min-heap.
        """

        min_heap: list = []
        heapify(min_heap)

        character_frequencies: Counter = Counter(input_data)

        for character, frequency in character_frequencies.items():
            # character is required to have a unique order
            heappush(min_heap, (frequency, character, BinaryTreeNode(character)))

        return min_heap

    def create_binary_tree(self: object, min_heap_priority_queue: list) -> Union[BinaryTree, None]:
        """
        Build the binary tree.

        Parameters
        ----------
        min_heap_priority_queue: list, required 
            The min-heap priority queue.

        Returns
        ----------
        Union[BinaryTree, None]
            Returns the binary tree or None.
        """
        if len(min_heap_priority_queue) > 0:
            #print(f"Queue has '{len(min_heap_priority_queue)}' items...")
            if len(min_heap_priority_queue) > 1:
                while len(min_heap_priority_queue) > 1:
                    lowest_frequency_item: tuple = heappop(
                        min_heap_priority_queue)
                    second_lowest_frequency_item: tuple = heappop(
                        min_heap_priority_queue)

                    internal_node_value: int = lowest_frequency_item[0] + \
                        second_lowest_frequency_item[0]
                    internal_node: BinaryTreeNode = BinaryTreeNode(
                        internal_node_value)
                    internal_node.set_left_child(lowest_frequency_item[2])
                    internal_node.set_right_child(
                        second_lowest_frequency_item[2])
                    internal_node_tuple: tuple = (
                        internal_node_value, f"{lowest_frequency_item[1]}{second_lowest_frequency_item[1]}", internal_node)

                    heappush(min_heap_priority_queue,
                             internal_node_tuple)

            binary_tree: BinaryTree = BinaryTree(
                heappop(min_heap_priority_queue)[2])
            # print(binary_tree.tree_to_list())
            return binary_tree
        else:
            #print("Queue is empty...")
            return

    def encode_input_data(self: object, input_data: str, binary_tree: BinaryTree) -> str:
        """
        Encode the input data.

        Parameters
        ----------
        input_data: str, required
            The input data as string.

        binary_tree: BinaryTree, required
            The binary tree used for encoding.

        Returns
        ----------
        str
            Returns the input data string encoded.
        """

        binary_representation: str = ""
        if input_data:
            cache: dict = {}
            for character in input_data:
                #print(f"Working with character '{character}'...")
                if character in cache:
                    #print("In cache...")
                    binary_for_character: str = cache[character]
                else:
                    #print("Not in cache...")
                    binary_for_character: str = self.create_binary_for_character(
                        binary_tree.get_root(), character) 
                    cache[character] = binary_for_character
                #print(f"Binary is '{binary_for_character}'...")
                binary_representation += binary_for_character

        return binary_representation

    def create_binary_for_character(self: object, root: BinaryTreeNode, character: str) -> str:
        """
        Create the binary representation for a character based on the tree.

        Parameters
        ----------
        root: BinaryTreeNode, required
            The binary tree root node.

        character: str, required
            The character to create the binary representation for.

        Returns
        ----------
        str
            Returns the binary representation. 
            Returns 2 if there is only a root node.
        """
        binary_representation: str = ""
        if (root.left is None) and (root.right is None):
            #print("Tree has only root node...")
            binary_representation = "2"
        else:
            #print("Tree has more than root node...")
            reversed_result: list = self.path_from_node_to_root(
                root, character)
            result: list = list(reversed(reversed_result))
            binary_representation = "".join(result)
        return binary_representation

    def path_from_node_to_root(self: object, root: BinaryTreeNode, character: str) -> Union[list, None]:
        """
        Get the path as binary representation to a character of interest.

        Parameters
        ----------
        root: BinaryTreeNode, required
            A binary tree node.

        character: str, required
            The character to search for.

        Returns
        ----------
        Union[list, None]
            Returnes the binary elements as list or None.
        """

        if root is None:
            return None
        elif root.value == character:
            return []

        left_answer: list = self.path_from_node_to_root(root.left, character)
        if left_answer is not None:
            left_answer.append("0")
            return left_answer

        right_answer = self.path_from_node_to_root(root.right, character)
        if right_answer is not None:
            right_answer.append("1")
            return right_answer

        return None
