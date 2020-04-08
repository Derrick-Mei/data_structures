from doubly_linked_list import DoublyLinkedList, ListNode


class LRUCache:
    """
    Our LRUCache class keeps track of:
    1. the max number of nodes it can hold,
    2. the current number of nodes it is holding,
    3. a doubly-linked list that holds the key-value entries in the correct order,
    4. a storage dict to store nodes (nodes store key-value pair)
    """

    def __init__(self, limit=10):
        self.limit = limit
        self.size = 0
        self.list = DoublyLinkedList()
        self.dict = {}

    def __str__(self):
        output = ''
        for key in (self.dict):
            output += self.dict[key].value.get(key)
        return output

    """
    1. Retrieves the value associated with the given key.
        a. return None if key doesn't exist
    2. move the key-value pair to the end of the list
    """

    def get(self, key):
        node = self.dict.get(key, None)

        if node == None:
            return None
        else:
            self.list.move_to_end(node)
            return node.value.get(key)

    """
    Adds the given key-value pair to the cache. The newly-
    added pair should be considered the most-recently used
    entry in the cache. If the cache is already at max capacity
    before this entry is added, then the oldest entry in the
    cache needs to be removed to make room. Additionally, in the
    case that the key already exists in the cache, we simply
    want to overwrite the old value associated with the key with
    the newly-specified value.
    """

    def set(self, key, value):
        # check if key exists,
        # if it does, update value and move to end
        # if key doesn't exist check size
        # if size = limit delete
        # add node
        # NOT PASSING TESTS
        node = self.dict.get(key, None)

        if node != None:
            node.value[key] = value
            print(node)
            self.list.move_to_end(node)
        else:
            if self.size == self.limit:
                head_node = self.list.remove_from_head()
                self.size -= 1
                head_node_key = list(head_node.keys())[0]
                del self.dict[head_node_key]
            self.list.add_to_tail({key: value})
            self.dict[key] = ListNode({key: value})
            self.size += 1
