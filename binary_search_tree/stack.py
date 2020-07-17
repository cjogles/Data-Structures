"""
A stack is a data structure whose primary purpose is to store and
return elements in Last In First Out order.

1. Implement the Stack class using an array as the underlying storage structure.
   Make sure the Stack tests pass.
2. Re-implement the Stack class, this time using the linked list implementation
   as the underlying storage structure.
   Make sure the Stack tests pass.
3. What is the difference between using an array vs. a linked list when
   implementing a Stack?
"""
from node import Node
from node import LinkedList

# ARRAY IMPLEMENTATION
class Stack:
    def __init__(self):
        self.stack = []

    def __repr__(self):
        return (f"stack = {self.stack}")

    def __len__(self):
        return len(self.stack)

    def push(self, value):
        self.stack.append(value)

    def pop(self):
        if self.stack.__len__() == 0:
            pass
        else:
            value = self.stack[len(self.stack) - 1]
            self.stack.pop()
            return value

# LINKED LIST IMPLEMENTATION
# class Stack:
#     def __init__(self):
#         self.size = 0
#         self.stack = LinkedList()

#     def __len__(self):
#         return self.size

#     def push(self, value):
#         self.stack.add_to_tail(value)
#         self.size += 1

#     def pop(self):
#         if self.size == 0:
#             pass
#         else:
#             self.size -= 1
#             return self.stack.remove_tail()


# Difference?

# A stack is a last in first out (LIFO) data structure. Currenlty all that is being
# tested in my stack folder is pushing an item on the end, popping an item off on the end,
# and getting the length of the storage. When using an array, all of those operations
# are constant time. O(1). When using a linked list, getting the length of the storage is
# linear because i will need to traverse the entire data structure to find out how
# big it is.
