class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        sum = (n+1)*n/2
        for num in nums:
            sum -= num
        return sum

class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        result = n
        i = 0
        for num in nums:
            result ^= num
            result ^= i
            i += 1
        return result
