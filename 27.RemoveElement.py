class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        p, q = 0, 0
        for p in range(len(nums)):
            if nums[p]!=val:
                nums[q]=nums[p]
                q += 1
        return q
