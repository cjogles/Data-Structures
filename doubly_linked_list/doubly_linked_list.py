"""
Each ListNode holds a reference to its previous node
as well as its next node in the List.
"""


class ListNode:
    def __init__(self, value, prev=None, next=None):
        self.prev = prev
        self.value = value
        self.next = next


"""
Our doubly-linked list class. It holds references to 
the list's head and tail nodes.
"""

class DoublyLinkedList:
    def __init__(self, node=None):
        self.head = node
        self.tail = node
        self.length = 1 if node is not None else 0

    def __len__(self):
        return self.length

    """
    Wraps the given value in a ListNode and inserts it 
    as the new head of the list. Don't forget to handle 
    the old head node's previous pointer accordingly.
    """

    def add_to_head(self, value):
        new_node = ListNode(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node 
            self.head = new_node
        self.length += 1

    """
    Removes the List's current head node, making the
    current head's next node the new head of the List.
    Returns the value of the removed Node.
    """

    def remove_from_head(self):
        if self.length == 0:
            return
        old_head = self.head
        if self.head.next is not None:
            self.head.next.prev = None
            self.head = self.head.next
        else:
            self.head = None
            self.tail = None
        self.length -= 1
        return old_head.value

    """
    Wraps the given value in a ListNode and inserts it 
    as the new tail of the list. Don't forget to handle 
    the old tail node's next pointer accordingly.
    """

    def add_to_tail(self, value):
        new_node = ListNode(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1

    """
    Removes the List's current tail node, making the 
    current tail's previous node the new tail of the List.
    Returns the value of the removed Node.
    """

    def remove_from_tail(self):
        if self.length == 0:
            return
        tail_value = self.tail.value
        self.delete(self.tail)
        return tail_value

    """
    Removes the input node from its current spot in the 
    List and inserts it as the new head node of the List.
    """

    def move_to_front(self, node):
        temp = node.value
        self.delete(node)
        self.add_to_head(temp)

    """
    Removes the input node from its current spot in the 
    List and inserts it as the new tail node of the List.
    """

    def move_to_end(self, node):
        temp = node.value
        self.delete(node)
        self.add_to_tail(temp)

    """
    Deletes the input node from the List, preserving the 
    order of the other elements of the List.
    """

    def delete(self, node):
        self.length -= 1
        if self.head == self.tail:
            self.head = None
            self.tail = None
            return
        if node == self.head:
            self.head = self.head.next
            self.head.prev = None
            return
        if node == self.tail:
            self.tail = self.tail.prev 
            self.tail.next = None
            return
        else:
            node.next.prev = node.prev
            node.prev.next = node.next 


    """
    Finds and returns the maximum value of all the nodes 
    in the List.
    """

    def get_max(self):
        # create a max_value variable set = self.head.value
        # iterate over every node and check if value is greater then max_value
        # if it is, max_value = that node value
        # your loop is going from head to tail
        # if currentnode.next != None
        # return value
        max_value = self.head.value
        current_node = self.head
        while (current_node.next != None):
            if current_node.value > max_value:
                max_value = current_node.value
            else:
                current_node = current_node.next
        if current_node.value > max_value:
            max_value = current_node.value
        return max_value





















# MY DELETE CODE
        # if self.length == 0:                            # EMPTY DLL CONDITION
        #     return None # node doesnt exist in DLL, FINISHED
        # elif self.length == 1:                          # 1 ITEM IN DLL CONDITION
        #     if self.head == node and self.tail == node:
        #         self.head = None
        #         self.tail = None
        #         self.length = 0
        #         return "deleted when there was only one item in DLL" # FINISHED
        # else:                                           # MULTIPLE ITEMS IN DLL CONDITION
        #     current_node = self.head
        #     while current_node != self.tail:
        #         if current_node == node:
        #             if current_node == self.head:
        #                 next_node = current_node.next 
        #                 self.head.next = None
        #                 self.head.prev = None
        #                 self.head = None
        #                 next_node.prev = None
        #             else:
        #                 prev_node = current_node.prev 
        #                 next_node = current_node.next 
        #                 current_node.next = None
        #                 current_node.prev = None
        #                 current_node = None
        #                 prev_node.next = next_node
        #                 next_node.prev = prev_node
        #             self.length -= 1
        #             return 0 # FINISHED
        #         else:
        #             current_node = current_node.next
                
        #     if current_node == self.tail:
        #         prev_node = current_node.prev 
        #         self.tail.next = None
        #         self.tail.prev = None
        #         self.tail = None
        #         prev_node.next = None
        #         self.length -= 1
        #         return 0 # FINISHED
        #     else:
        #         return None # node doesnt exist in DLL, FINISHED

# my add to tail code
        # my_node = ListNode(value)
        # if (self.length == 0):
        #     self.head = my_node
        #     self.tail = my_node
        # else:
        #     old_tail = self.tail
        #     old_tail.next = my_node
        #     self.tail = my_node
        #     self.tail.prev = old_tail
        # self.length += 1

# the node before NODE -> change next