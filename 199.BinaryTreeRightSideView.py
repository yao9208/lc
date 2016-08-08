# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def rightSideView(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        result = []
        self.helper(root, result, 0)
        return result

    def helper(self, root, result, level):
        if not root:
            return
        if len(result)==level:
            result.append(root.val)
        self.helper(root.right, result, level+1)
        self.helper(root.left, result, level+1)
