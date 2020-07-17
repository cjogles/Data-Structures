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

from queue import Queue
from stack import Stack

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
        fn(self.value)
        if self.left:
            self.left.for_each(fn)
        if self.right:
            self.right.for_each(fn)

# Part 2 -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    def in_order_print(self, node):
        # if the current node is None
        # we know we've reached the end of a recursion
        # (base case) we want to return
        # check if we can "move left"
        # visit the node by printing its value
        # check if we can "move right"
        if self is None:
            return
        if self.left is not None:
            self.left.in_order_print(self.left)
        print(self.value)
        if self.right is not None:
            self.right.in_order_print(self.right)

    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    def bft_print(self, node):
        # You should import the queue class from earlier in the
        # week and use that class to implement this method
        # Use a queue to form a "line", for the nodes to "get in"
        # start by placing the root in the queue
        # while length of queue is greater than 0
        # dequeue item from front of queue
        # print that item
        # place current item's left node in queue if not None
        # place current item's right node in queue if not None
        line = Queue()
        line.enqueue(node)
        while line.__len__() > 0:
            my_value = line.dequeue()
            print(my_value.value)
            if my_value.left:
                line.enqueue(my_value.left)
            if my_value.right:
                line.enqueue(my_value.right)
            
    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    def dft_print(self, node):
        pass
        # initialize an empty stack
        # push the root node onto the stack
        # need a while loop to manager our iteration
        # if stack is not empty enter the while loop
        # pop top item off the stack
        # print that item's value
        # if there is a right subtree
        # push right item onto the stack
        # if there is a left subtree
        # push left item onto the stack
        stack = Stack()
        stack.push(node)
        while stack.__len__() > 0:
            my_value = stack.pop()
            print(my_value.value)
            if my_value.right:
                stack.push(my_value.right)
            if my_value.left:
                stack.push(my_value.left)


    # Stretch Goals -------------------------------------------------------------------------------
    # Note: Research may be required

    # Print Pre-order recursive DFT

    def pre_order_dft(self, node):
        pass

    # Print Post-order recursive DFT
    def post_order_dft(self, node):
        pass


# line = Queue()
# line.enqueue(1)
# line.enqueue(2)
# line.enqueue(3)
# print(line)
