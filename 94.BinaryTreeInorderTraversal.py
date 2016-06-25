# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from collections import deque
class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        stack = deque()
        node = root
        result = []
        while node or len(stack)!=0:
            while node:
                stack.append(node)
                node = node.left
            cur = stack.pop()
            result.append(cur.val)
            node = cur.right
        return result
             
