import random
class RandomizedSet(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.arr = []
        self.dic = {}

    def insert(self, val):
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        :type val: int
        :rtype: bool
        """
        if val in self.dic:
            return False
        self.arr.append(val)
        self.dic[val] = len(self.arr)-1
        return True


    def remove(self, val):
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        :type val: int
        :rtype: bool
        """
        if val not in self.dic:
            return False
        idx = self.dic[val]
        if idx!=len(self.arr)-1:
            self.dic[self.arr[-1]] = idx
            self.arr[idx], self.arr[-1] = self.arr[-1], self.arr[idx]
        del self.arr[-1] #don't forget to delete
        del self.dic[val]
        return True


    def getRandom(self):
        """
        Get a random element from the set.
        :rtype: int
        """
        next = random.randint(0, len(self.arr)-1)
        return self.arr[next]



# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
