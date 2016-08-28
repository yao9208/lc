class Solution(object):
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        cur, last, step = 0, 0, 0
        for i in range(len(nums)):
            if i > last:
                step += 1
                last = cur
            cur = max(cur, nums[i]+i)
        return step
