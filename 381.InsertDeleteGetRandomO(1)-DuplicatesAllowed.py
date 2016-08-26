from collections import defaultdict
import random
class RandomizedCollection(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.arr = []
        self.dic = defaultdict(set)

    def insert(self, val):
        """
        Inserts a value to the collection. Returns true if the collection did not already contain the specified element.
        :type val: int
        :rtype: bool
        """
        flag = val not in self.dic
        self.arr.append(val)
        self.dic[val].add(len(self.arr)-1)
        return flag


    def remove(self, val):
        """
        Removes a value from the collection. Returns true if the collection contained the specified element.
        :type val: int
        :rtype: bool
        """
        dic = self.dic
        n = len(self.arr)
        if val not in dic:
            return False
        idx = dic[val].pop()
        if len(dic[val])==0:
            del dic[val]

        if idx!=n-1:
            num = self.arr[n-1]
            dic[num].remove(n-1)
            dic[num].add(idx)
            self.arr[-1], self.arr[idx] = self.arr[idx], self.arr[-1]
        del self.arr[-1]
        return True


    def getRandom(self):
        """
        Get a random element from the collection.
        :rtype: int
        """
        next = random.randint(0, len(self.arr)-1)
        return self.arr[next]


# Your RandomizedCollection object will be instantiated and called as such:
# obj = RandomizedCollection()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
