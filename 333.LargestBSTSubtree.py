# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    result = 0
    def largestBSTSubtree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.helper(root)
        return self.result

    def helper(self, root):
        if not root:
            return 0, sys.maxint, -sys.maxint
        left = self.helper(root.left)
        right = self.helper(root.right)
        if left[0]==-1 or right[0]==-1:
            return -1, None, None
        if root.val<=left[2] or root.val>=right[1]:
            return -1, None, None
        num = left[0]+right[0]+1
        self.result = max(num, self.result)
        return num, min(left[1], root.val), max(right[2], root.val)
        
