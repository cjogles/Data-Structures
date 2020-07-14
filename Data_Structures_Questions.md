Answer the following questions for each of the data structures you implemented as part of this project.

## Stack (Last in First Out)

1. What is the runtime complexity of `push` using a list?
    O(n) - because worst case scenario with a dynamic array you will 
           need to double the list at times. usually will be O(1) though. 
2. What is the runtime complexity of `push` using a linked list?
    O(1) - No need to reference any other 
           node except the tail
3. What is the runtime complexity of `pop` using a list?
    O(1) - worst case scenario never includes doubling the array, so its constant. 
4. What is the runtime complexity of `pop` using a linked list?
    O(n) - we have the tail reference to use so we can pop it, but we still need to traverse the whole list
           to reset the pointer of the node prev to the original tail and set that prev_node_pointer to none
5. What is the runtime complexity of `len` using a list?
    O(1) - len method for list returns a variable. thats constant time. 
6. What is the runtime complexity of `len` using a linked list?
    O(1) - because we wrote a counter that keeps track of the variable size, it is constant. 

## Queue (First in First Out)
1. What is the runtime complexity of `enqueue` using a list?
    O(n) - because we may need to double the size of the list (i.e. array)
2. What is the runtime complexity of `enqueue` using a linked list?
    O(1) - constant because we know where the tail is. 
3. What is the runtime complexity of `dequeue` using a list?
    O(n) - because we would need to change the index of every single item.
4. What is the runtime complexity of `dequeue` using a linked list?
    O(1) - we have reference to the head, which we can remove easily.
           and the head pointer points to the next node, so we can reference that node 
           and set it to become the new head. 
5. What is the runtime complexity of `len` using a list?
    O(1) - len method for list returns a variable. thats constant time. 
6. What is the runtime complexity of `len` using a linked list?
    O(1) - because we wrote a counter that keeps track of the variable size, it is constant. 

## Doubly Linked List

1. What is the runtime complexity of `ListNode.insert_after`?

2. What is the runtime complexity of `ListNode.insert_before`?

3. What is the runtime complexity of `ListNode.delete`?

4. What is the runtime complexity of `DoublyLinkedList.add_to_head`?

5. What is the runtime complexity of `DoublyLinkedList.remove_from_head`?

6. What is the runtime complexity of `DoublyLinkedList.add_to_tail`?

7. What is the runtime complexity of `DoublyLinkedList.remove_from_tail`?

8. What is the runtime complexity of `DoublyLinkedList.move_to_front`?

9. What is the runtime complexity of `DoublyLinkedList.move_to_end`?

10. What is the runtime complexity of `DoublyLinkedList.delete`?

    a. Compare the runtime of the doubly linked list's `delete` method with the worst-case runtime of the JS `Array.splice` method. Which method generally performs better?

## Binary Search Tree

1. What is the runtime complexity of `insert`? 

2. What is the runtime complexity of `contains`?

3. What is the runtime complexity of `get_max`? 

4. What is the runtime complexity of `for_each`?
    
## Heap

1. What is the runtime complexity of `_bubble_up`?

2. What is the runtime complexity of `_sift_down`?

3. What is the runtime complexity of `insert`?

4. What is the runtime complexity of `delete`?

5. What is the runtime complexity of `get_max`?
