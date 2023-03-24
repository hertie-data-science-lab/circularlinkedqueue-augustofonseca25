# -*- coding: utf-8 -*-
"""
Created on Tue Mar 14 15:42:53 2023


@author: Hannah
"""

class Empty(Exception):
  pass



class CircularQueue:
    """Queue implementation using circularly linked list for storage"""""

    class _Node:
        __slots__ = '_element', '_next'

        def __init__(self, data, nxt = None):
            self._element = data
            self._next = nxt

    def __init__(self):
        self._head = None
        self._size = 0

    def __len__(self):
        return self._size

    def is_empty(self):
        return self._size == 0

    # Method to deque an element
    def dequeue(self):
        ''''
        Removes the first element of the list
        '''
        old_head = self._head
        if self.is_empty: # Check if the list is empty
            raise Exception("List is empty") # the list is empty, raise an exception

        if self._size == 1: # Check if the list contains only the head.
            self._head = None # Since the list only contains the head, set it to None to remove it
        else:
            self._head = self._head._next #the next node will become the new head
        '''
        # Decreases list size by 1 and return the old head
        '''
        self._size -= 1 # Decreases list size by 1
        print("Element removed from the list head")


    def first(self): #Method to get the head node
        '''
        Returns the element that is currently at the head of the queue. Raises an exception if the queue is empty.
        '''
        if self.is_empty(): # Check if the head node is empty
            raise Exception("List is empty")
        else: #If it`s not empty, returns the head node
            return self._head



    def enqueue (self, string):
        '''
        Adds an element to the back of the queue. Raises an exception if the queue is empty.
        '''
        new_node = self._Node(string)
        current_node = self._head  # set a current_node with the element in the head position

        if self.is_empty(): # Check if the list is empty
            self._head = new_node # The head will be the new node
            new_node._next = self # The own node is the next one
            print("The new NODE is", new_node._element)
            print("The new head is", self._head._element)
            print("The next element is", self._head._next)
        else: # If the list was not empty, traverse it fo find the 2nd last node
            # Traverse the nodes comparing each next node with the head, to find the second last one
            while current_node._next != self.first(): # Go throught it until the next attribute points to the head.
                current_node = current_node._next # the current_node becomes the next node

            # When you find the last node
            new_node._next = self._head # the new node next attribute points to the head
            current_node._next = new_node # the last node next attribute points to the new node
        '''
        In any case, increment the list size
        '''
        self._size += 1  # Increment list size by 1
        print("Element added to the list tail")

    def rotate(self):
        '''
        Rotate the queue: effectively transfer the item at the head of the list to the tail of the list
        '''
        if not self.is_empty(): # Check if the list is empty
            self._head = self._head._next # the new head will be the 2nd node of the list
            print("ROTATION: The head was moved to the tail. The new head i", self._head._element)


cq = CircularQueue()
print("Starting Size", len(cq) )
cq.enqueue("a")
cq.enqueue("b")
cq.enqueue("c")
print("Current Size", len(cq) )
print("Current Head", cq.first())
cq.rotate()
print("Current Head after rotating", cq.first())
