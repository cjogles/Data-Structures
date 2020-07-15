"""
Binary search trees are a data structure that enforce an ordering over
the data they store. That ordering in turn makes it a lot more efficient
at searching for a particular piece of data in the tree.

This part of the project comprises two days:
1. Implement the methods `insert`, `contains`, `get_max`, and `for_each`
   on the BSTNode class.
2. Implement the `in_order_print`, `bft_print`, and `dft_print` methods
   on the BSTNode class.
"""


class BSTNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):
        # case1 value is less then self.value
        if value < self.value:
            # if there is no left child, insert here
            if self.left is None:
                self.left = BSTNode(value)
            # else
            else:
                # repeat the process on left subtree (recursive action)
                # self.left.insert(value)
                self.left.insert(value)

        # case2 value is greater then or equal to self.value
        elif value >= self.value:
            if self.right is None:
                self.right = BSTNode(value)
            else:
                self.right.insert(value)

    # Return True if the tree contains the value
    # False if it does not

    def contains(self, target):
        pass
        # case1 if self.value is equal to target
        # return true
        if self.value == target:
            return True
        # case2 if target is less then self.value:
            # if self.left is None:
            # it isn't in the tree! return false
            # else:
            # return self.left.contains(target) bound instance is left node
        if target < self.value:
            if self.left is None:
                return False
            else:
                return self.left.contains(target)
        # case3 if target is greater then or equal to self.value:
            # if self.right is None:
                # return false
            # else:
                # return self.right.contains(target)
        if target >= self.value:
            if self.right == None:
                return False
            else:
                return self.right.contains(target)

    # Return the maximum value found in the tree
    def get_max(self):
        # version1
        # current_node = self
        # while (current_node.right):
        #     current_node = current_node.right
        # return current_node.value
        # version2
        if self.right != None:
            return self.right.get_max()
        return self.value

    # Call the function `fn` on the value of each node
    def for_each(self, fn):
        if self != None:
            fn(self.value)
        if self.right:
            fn(self.right)
            self.right.for_each(fn)
        if self.left:
            fn(self.left)
            self.left.for_each(fn)

    # Part 2 -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    def in_order_print(self, node):
        pass

    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    def bft_print(self, node):
        pass

    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    def dft_print(self, node):
        pass

    # Stretch Goals -------------------------
    # Note: Research may be required

    # Print Pre-order recursive DFT
    def pre_order_dft(self, node):
        pass

    # Print Post-order recursive DFT
    def post_order_dft(self, node):
        pass


jackson = BSTNode(2)
print(jackson.get_max())
