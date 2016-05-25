# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def closestValue(self, root, target):
        """
        :type root: TreeNode
        :type target: float
        :rtype: int
        """
        ret = root.val
        while root is not None:
            if abs(target-root.val) < abs(ret - target):
                ret = root.val
            if root.val > target:
                root = root.left
            else:
                root = root.right
        return ret

# recursive way?
