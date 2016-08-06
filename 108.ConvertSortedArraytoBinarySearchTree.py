class Solution(object):
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        if nums is None:
            return None
        return self.build(nums, 0, len(nums)-1)

    def build(self, nums, start, end):
        if start>end:
            return None
        mid = (start+end)/2
        root = TreeNode(nums[mid])
        root.left = self.build(nums, start, mid-1)
        root.right = self.build(nums, mid+1, end)
        return root
