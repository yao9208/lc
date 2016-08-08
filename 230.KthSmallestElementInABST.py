# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        left = self.count(root.left)
        if left==k-1:
            return root.val
        if left<k-1:
            return self.kthSmallest(root.right, k-left-1)
        else:
            return self.kthSmallest(root.left, k)

    def count(self, root):
        if not root:
            return 0
        return 1 + self.count(root.left) + self.count(root.right)
