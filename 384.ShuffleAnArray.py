import random
class Solution(object):

    def __init__(self, nums):
        """

        :type nums: List[int]
        :type size: int
        """
        self.arr = nums

    def reset(self):
        """
        Resets the array to its original configuration and return it.
        :rtype: List[int]
        """
        return self.arr

    def shuffle(self):
        """
        Returns a random shuffling of the array.
        :rtype: List[int]
        """
        n = len(self.arr)
        bound = [ (x, random.random()) for x in self.arr]
        bound.sort(key=lambda x:x[1])
        return [x[0] for x in bound]
