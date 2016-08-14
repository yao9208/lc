class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        result = []
        cur = []
        self.helper(result, cur, 0, nums)
        return result

    def helper(self, result, cur, start, nums):
        result.append(cur[:])
        n = len(nums)
        for i in range(start, n):
            cur.append(nums[i])
            self.helper(result, cur, i+1, nums)
            del cur[-1]
