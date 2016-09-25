# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        stack = []
        res = []
        prev, cur = None, None
        if not root:
            return res
        stack.append(root)
        while len(stack)>0:
            cur = stack[-1]
            if prev is None or cur==prev.left or cur==prev.right:
                if cur.left:
                    stack.append(cur.left)
                elif cur.right:
                    stack.append(cur.right)
            elif cur.left==prev:
                if cur.right:
                    stack.append(cur.right)
            else:
                res.append(cur.val)
                stack.pop()
            prev = cur
        return res
