class Node(object):
    def __init__(self, key, x):
        self.key = key
        self.val = x
        self.prev = None
        self.next = None

class LRUCache(object):

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.dic = {}
        self.room = capacity
        self.head = Node(0, 0)
        self.tail = Node(0, 0)
        self.head.next = self.tail
        self.tail.prev = self.head

    def insert(self, key, value):
        if self.room == 0:
            self.evict()
        prev = self.tail.prev
        tail = self.tail
        node = Node(key, value)
        prev.next = node
        node.next = tail
        tail.prev = node
        node.prev = prev
        self.dic[key] = node
        self.room -= 1

    def evict(self):
        head = self.head
        node = head.next
        key = node.key
        del self.dic[key]
        next = node.next
        head.next = next
        next.prev = head
        self.room += 1

    def moveToTail(self, key):
        node = self.dic[key]
        prev = node.prev
        next = node.next
        prev.next = next
        next.prev = prev

        tail = self.tail
        prev = tail.prev
        prev.next = node
        node.next = tail
        tail.prev = node
        node.prev = prev

    def get(self, key):
        """
        :rtype: int
        """
        if key in self.dic:
            self.moveToTail(key)
            return self.dic[key].val
        return -1

    def set(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: nothing
        """
        if key in self.dic:
            node = self.dic[key]
            node.val = value
            self.moveToTail(key)
        else:
            self.insert(key, value)
