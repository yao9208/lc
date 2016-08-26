class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dic = {}
        result = 0
        for n in nums:
            if n not in dic:
                left, right = 0, 0
                if n-1 in dic:
                    left = dic[n-1]
                if n+1 in dic:
                    right = dic[n+1]
                len = left + right +1
                dic[n] = dic[n-left] = dic[n+right] = len
                result = max(result, len)
        return result



class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums = set(nums)
        result = 0
        for n in nums:
            if n-1 not in nums:
                m = n+1
                while m in nums:
                    m += 1
                cur = m-n
                result = max(result, cur)
        return result
