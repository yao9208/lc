# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
import sys
class Solution(object):
    result = -sys.maxint
    def maxPathSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.maxPathDown(root)
        return self.result

    def maxPathDown(self, root):
        if not root:
            return 0
        left = max(0, self.maxPathDown(root.left))
        right = max(0, self.maxPathDown(root.right))
        self.result = max(self.result, left+right+root.val)
        return max(left, right) + root.val
