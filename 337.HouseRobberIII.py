# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def rob(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        num = self.helper(root)
        return max(num)

    def helper(self, root):
        if not root:
            return 0, 0
        left = self.helper(root.left)
        right = self.helper(root.right)
        result = [0, 0]
        result[0] = root.val + left[1] + right[1]
        result[1] = max(left[0], left[1]) + max(right[0], right[1])
        return result

                
