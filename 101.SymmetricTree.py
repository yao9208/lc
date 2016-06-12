# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root:
            return True
        return self.mirror(root.left, root.right)

    def mirror(self, p, q):
        if not p and not q:
            return True
        if not p or not q:
            return False
        else:
            return p.val == q.val and self.mirror(p.left, q.right) and self.mirror(p.right, q.left)
