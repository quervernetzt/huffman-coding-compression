from solution.binary_tree import BinaryTree, BinaryTreeNode

class HuffmanDecoding(object):
    def __init__(self: object):
        """
        Constructor.
        """
        pass

    def decode(self: object, string_to_decode: str, binary_tree: BinaryTree) -> str:
        """
        Decode the input string using the binary tree.

        Parameters
        ----------
        string_to_decode: str, required
            The string to decode.
        
        binary_tree: BinaryTree, required
            The binary used for decoding.

        Returns
        ----------
        str
            The decoded string.
        """

        decoded_string: str = ""
        if string_to_decode and binary_tree:
            #print("Input string and binary tree are not empty / None...")
            current_node: BinaryTreeNode = binary_tree.get_root()

            if string_to_decode == "2":
                decoded_string = current_node.value
            else:
                while len(string_to_decode) > 0:
                    while current_node.has_left_child() and current_node.has_right_child():
                        current_binary = string_to_decode[0]
                        string_to_decode = string_to_decode[1:]
                        #print(f"Working with binary '{current_binary}'...")

                        if current_binary == "0":
                            #print("Moving left...")
                            current_node = current_node.get_left_child()
                        elif current_binary == "1":
                            #print("Moving right...")
                            current_node = current_node.get_right_child()
                        else:
                            raise Exception("Current binary is invalid...")
                    decoded_string += current_node.value
                    current_node = binary_tree.get_root()
        else:
            #print("Input string or binary tree are empty / None...")
            pass
            
        return decoded_string
        

            

