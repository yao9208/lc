from sets import Set
class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        dic = Set()
        for n in nums:
            if n in dic:
                return True
            else:
                dic.add(n)
        return False
