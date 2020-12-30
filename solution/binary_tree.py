from typing import Union

class BinaryTreeNode(object):
    def __init__(self: object, value: object = None) -> None:
        """
        Constructor.

        Parameters
        ----------
        value: object, optional 
            The value to be set for the node.
        """
        self.value: object = value
        self.left: BinaryTreeNode = None
        self.right: BinaryTreeNode = None

    def get_value(self: object) -> object:
        """
        Get the value of the node.

        Returns
        ----------
        object
            Returns the value of the node.
        """
        return self.value

    def set_value(self, value: object) -> None:
        """
        Set the value of the node.

        Parameters
        ----------
        value: object, required 
            The value to be set for the node.
        """
        self.value: object = value

    def set_left_child(self: object, left_node: 'BinaryTreeNode') -> None:
        """
        Set the left child of the node.

        Parameters
        ----------
        left_node: BinaryTreeNode, required 
            The node to be set as left child.
        """
        self.left: BinaryTreeNode = left_node

    def set_right_child(self: object, right_node: 'BinaryTreeNode') -> None:
        """
        Set the right child of the node.

        Parameters
        ----------
        right_node: BinaryTreeNode, required 
            The node to be set as right child.
        """
        self.right: BinaryTreeNode = right_node

    def get_left_child(self: object) -> 'BinaryTreeNode':
        """
        Get the left child node.

        Returns
        ----------
        BinaryTreeNode
            The left child node.
        """
        return self.left

    def get_right_child(self: object) -> 'BinaryTreeNode':
        """
        Get the right child node.

        Returns
        ----------
        BinaryTreeNode
            The right child node.
        """
        return self.right

    def has_left_child(self: object) -> bool:
        """
        Check if node has left child.

        Returns
        ----------
        bool
            Returns True if node has left child, else False
        """
        return self.left is not None

    def has_right_child(self: object) -> bool:
        """
        Check if node has right child.

        Returns
        ----------
        bool
            Returns True if node has left child, else False
        """
        return self.right is not None


class BinaryTree(object):
    def __init__(self: object, root_node: BinaryTreeNode) -> None:
        """
        Constuctor.

        Parameters
        ----------
        root_node: BinaryTreeNode, required
            The root node of the binary tree
        """
        self.root: BinaryTreeNode = root_node

    def get_root(self: object) -> BinaryTreeNode:
        """
        Get root node of the binary tree.

        Returns
        ----------
        BinaryTreeNode:
            Returns the root node.
        """
        return self.root

    def tree_to_list(self: object) -> list:
        """
        Converts the tree to a list for debugging purposes.

        Returns
        ----------
        list:
            List with node values visited in order.
        """
        visit_order: list = []
        root: BinaryTreeNode = self.get_root()
            
        def traverse_tree(node: BinaryTreeNode) -> Union['traverse_tree', None]:
            if node:
                # Visit
                visit_order.append(node.get_value())
                # Traverse left
                traverse_tree(node.get_left_child())
                # Traverse right
                traverse_tree(node.get_right_child())
            
        traverse_tree(root)

        return visit_order
