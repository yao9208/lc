class Solution(object):
    def minSubArrayLen(self, s, nums):
        """
        :type s: int
        :type nums: List[int]
        :rtype: int
        """
        start, end = 0, 0
        cur = 0
        result = sys.maxint
        for i in range(len(nums)):
            cur += nums[i]
            while cur>=s:
                result = min(result, i-start+1)
                cur -= nums[start]
                start+=1
        if result == sys.maxint:
            return 0
        return result
