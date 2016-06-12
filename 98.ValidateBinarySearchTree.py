# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        return self.helper(root, None, None)

    def helper(self, root, upper, lower):
        if not root:
            return True
        if lower and root.val<=lower or upper and root.val>=upper:
            return False
        left, right = True, True
        if root.left:
            left = root.left.val<root.val and self.helper(root.left, root.val, lower)
        if root.right:
            right = root.right.val>root.val and self.helper(root.right, upper, root.val)
        return left and right
