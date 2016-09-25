class Solution(object):
    def maxCoins(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)+2
        nums = [1]+nums+[1]
        dp = [[0]*n for x in range(n)]
        return self.helper(dp, nums, 0, n-1)

    def helper(self, dp, nums, left, right):
        if left+1==right:
            return 0
        if dp[left][right]>0:
            return dp[left][right]
        res = 0
        for i in range(left+1, right):
            res = max(res, nums[left]*nums[i]*nums[right]+self.helper(dp, nums, left, i)+self.helper(dp, nums, i, right))
        dp[left][right] = res
        return res
