import sys
sys.path.append('../queue_and_stack')

from dll_stack import Stack
from dll_queue import Queue


class BinarySearchTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):
        # If no current value
        if self.value == None:
            self.value = value

        # If value < current value
        if value < self.value:
            if self.left == None:
                self.left = BinarySearchTree(value)
            else:
                self.left.insert(value)

        # if value is >= current value
        if value >= self.value:
            if self.right == None:
                self.right = BinarySearchTree(value)
            else:
                self.right.insert(value)

    # Return True if the tree contains the value
    # False if it does not

    def contains(self, target):

        if self.value == target:
            return True

        elif target > self.value:
            if self.right == None:
                return False
            else:
                return self.right.contains(target)

        elif target < self.value:
            if self.left == None:
                return False
            else:
                return self.left.contains(target)


    # Return the maximum value found in the tree
    def get_max(self):

        if self.right == None:
            return self.value
        else:
            return self.right.get_max()


    # Call the function `cb` on the value of each node
    # You may use a recursive or iterative approach
    def for_each(self, cb):
        cb(self.value)

        if self.left != None:
            self.left.for_each(cb)

        if self.right != None:
            self.right.for_each(cb)

