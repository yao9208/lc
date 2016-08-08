# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def sumNumbers(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        return self.helper(root, 0)

    def helper(self, root, num):
        if not root:
            return 0
        if not root.left and not root.right:
            return 10 * num + root.val
        return self.helper(root.left, 10*num+root.val) + self.helper(root.right, 10*num+root.val)
