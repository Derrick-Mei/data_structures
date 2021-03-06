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

    # DAY 2 Project -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    def in_order_print(self, node):
        if node.left != None:
            node.left.in_order_print(node.left)

        print(node.value)

        if node.right != None:
            node.right.in_order_print(node.right)


    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    def bft_print(self, node):
        if node is None:
            return
        q = Queue()
        q.enqueue(node)
        while q.size > 0:
            node = q.dequeue()
            print(node.value)
            if node.left is not None:
                q.enqueue(node.left)
            if node.right is not None:
                q.enqueue(node.right)

    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    def dft_print(self, node):

        # a recursive approach
        # if node is None:
        #     return
        # print(node.value)
        # if node.left != None:
        #     node.left.in_order_print(node.left)

        # if node.right != None:
        #     node.right.in_order_print(node.right)

        if node is None:
            return
        s = Stack()
        s.push(node)
        while s.size > 0:
            node = s.pop()
            print(node.value)
            if node.left is not None:
                s.push(node.left)
            if node.right is not None:
                s.push(node.right)

    # STRETCH Goals -------------------------
    # Note: Research may be required

    # Print Pre-order recursive DFT
    def pre_order_dft(self, node):
        # print from current node and traverse down
        print(node.value)
        if node.left is not None:
            self.pre_order_dft(node.left)
        if node.right is not None:
            self.pre_order_dft(node.right)

    # Print Post-order recursive DFT
    def post_order_dft(self, node):
        # traverse all the way and the print back up
        if node.left is not None:
            self.post_order_dft(node.left)
        if node.right is not None:
            self.post_order_dft(node.right)
        print(node.value)
