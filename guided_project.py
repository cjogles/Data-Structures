# Node: stores two pieces of data, the value and the pointer to the next node
#       needs to be able to get value, set value, get next, and set next
class Node:
    def __init__(self, value=None, next_node=None):
        self.value = value
        self.next_node = next_node

    def get_value(self):
        return self.value
    
    def set_value(self, value):
        self.value = value

    def get_next(self):
        return self.next_node

    def set_next(self, new_next):
        self.next_node = new_next

# Linked List: has references to the head and tail reference. 
#              append (add a new node to the node referenced by the tail) --> AddToTail 
#              prepend (add a new node and point that nodes next_node at the old head, update head pointer)
#              remove head
#              remove tail
#              contains?
#              get_max
#              get_min
class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def add_to_tail(self, value):
        new_node = Node(value)
        if self.head == None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.set_next(new_node)
            self.tail = new_node
    
    def remove_head(self):
        # empty LL
        if self.head == None:
            return None
        # LL of one item
        if self.head.get_next() is None:
            head = self.head
            self.head = None
            self.tail = None
            return head.get_value()
        # More then one item
        value = self.head.get_value()
        self.head = self.head.get_next()
        return value








"""
O(n) - Linear Time
"""
animals = ['Duck', 'Jackal', 'Hippo', 'Aardvark', 'Cat',
           'Flamingo', 'Iguana', 'Giraffe', 'Elephant', 'Bear']
​

def print_animals(animal_list):
    for i in range(len(animal_list)):
        print(animal_list[i])
​
​
"""
What about this one? What runtime complexity is this one? the next one?
"""
​
​
def print_animals(animal_list):
    for i in range(len(animal_list)):
        print(animal_list[i])
        my_number = 0
        for _ in range(100000):
            my_number += 1
​
def another_one(animal_list):
    print(animal_list[0])
# constant time O(1). as input size changes, how does the number of computations change? computation size doesn't change! so constant time.
​
"""
CFU: Slack Thread: Why doesn't the nested for loop make the time complexity O(n^2)?
"""
​
​
"""
O(n^2) & O(n^3) - Polynomial Time
"""
animals = ['Duck', 'Jackal', 'Hippo', 'Aardvark', 'Cat',
           'Flamingo', 'Iguana', 'Giraffe', 'Elephant', 'Bear']
​
​
# Print a list of all possible animal pairs
def print_animal_pairs():
    for animal_1 in animals:
        for animal_2 in animals:
            print(f"{animal_1} - {animal_2}")
​
​
# Print a list of all possible animal triples
def print_animal_triples():
    for animal_1 in animals:
        for animal_2 in animals:
            for animal_3 in animals:
                print(f"{animal_1} - {animal_2} - {animal_3}")
​
​
# Print a list of all possible animal triples
def print_animal_triples():
    for animal in animals:
        print(animal)
​
    for animal_1 in animals:
        for animal_2 in animals:
            for animal_3 in animals:
                print(f"{animal_1} - {animal_2} - {animal_3}")
​
​
"""
CFU: Slack Thread
What's the time complexity to print all animal quintuples? What about "ten"tuples?
"""
​
​
"""
O(log n) - Logarithmic Time
"""
animals = ['Duck', 'Jackal', 'Hippo', 'Aardvark', 'Cat',
           'Flamingo', 'Iguana', 'Giraffe', 'Elephant', 'Bear']
​
​
# free all the animals, half at a time
# (remove them from the array)
def free_animals(animal_list):
    while len(animal_list) > 0:
        animal_list = animal_list[0: len(animal_list) // 2]
​
# We are reducing by half at each step
# This is the inverse of doubling at each step O(2^n) - Exponential Time
​
​
"""
CFU: Slack Thread
What's the worst the number of steps can get for a O(log n) time complexity
algorithm with an input size of 10 million?
"""
