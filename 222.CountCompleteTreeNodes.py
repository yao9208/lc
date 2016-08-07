# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def countNodes(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        node = root
        left, right = 0, 0
        while node:
            left += 1
            node = node.left
        node = root
        while node:
            right += 1
            node = node.right
        if left == right:
            return 2**left - 1
        else:
            return 1 + self.countNodes(root.left) + self.countNodes(root.right)
        
