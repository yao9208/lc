# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def hasPathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: bool
        """
        return self.helper(root, 0, sum)

    def helper(self, root, sum, target):
        if not root:
            return False
        if not root.left and not root.right:
            return root.val == target-sum
        left, right = False, False
        if root.left:
            left = self.helper(root.left, sum+root.val, target)
        if root.right:
            right = self.helper(root.right, sum+root.val, target)
        return left or right
