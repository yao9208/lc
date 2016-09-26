# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def sumOfLeftLeaves(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        stack = []
        if not root:
            return 0
        stack.append(root)
        prev = None
        result = 0
        while len(stack)>0:
            node = stack.pop()
            if prev and prev.left==node and not node.left and not node.right:
                result+=node.val
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)
            prev = node
        return result
