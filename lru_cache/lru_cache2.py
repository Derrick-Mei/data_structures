from doubly_linked_list import DoublyLinkedList, ListNode

class LRUCache:

    def __init__(self, limit=10):
        self.limit = limit
        self.order = DoublyLinkedList()
        self.storage = {}

    # def __str__(self):
    #     output = ''
    #     for key in (self.storage):
    #         output += self.storage[key].value.get(key)
    #     return output

    def get(self, key):
        node = self.storage.get(key, None)

        if node == None:
            return None
        else:
            self.order.move_to_end(node)
            return node.value[1]


    def set(self, key, value):

        # teacher implementation
        if key in self.storage:
            node = self.storage[key]
            node.value = (key, value)
            self.order.move_to_end(node)
            return

        if len(self.order) == self.limit:
            # key_of_oldest = self.order.head.value[0]
            # self.storage.pop(key_of_oldest)
            # self.order.remove_from_head()

            self.storage.pop(self.order.remove_from_head()[0])

        self.order.add_to_tail((key, value))
        self.storage[key] = self.order.tail
        self.order = DoublyLinkedList()
        self.storage = {}

    def __str__(self):
        output = ''
        for key in (self.storage):
            output += self.storage[key].value.get(key)
        return output

    """
    1. Retrieves the value associated with the given key.
        a. return None if key doesn't exist
    2. move the key-value pair to the end of the list
    """

    def get(self, key):
        node = self.storage.get(key, None)

        if node == None:
            return None
        else:
            self.order.move_to_end(node)
            return node.value[1]


    def set(self, key, value):

        # teacher implementation
        if key in self.storage:
            node = self.storage[key]
            node.value = (key, value)
            self.order.move_to_end(node)
            return

        if len(self.order) == self.limit:
            # key_of_oldest = self.order.head.value[0]
            # self.storage.pop(key_of_oldest)
            # self.order.remove_from_head()

            self.storage.pop(self.order.remove_from_head()[0])

        self.order.add_to_tail((key, value))
        self.storage[key] = self.order.tail