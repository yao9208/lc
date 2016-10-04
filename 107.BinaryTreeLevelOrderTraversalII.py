# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def levelOrderBottom(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        current = []
        next = []
        result = []
        if not root:
            return result
        current.append(root)
        while len(current)!=0:
            tmp = []
            for node in current:
                tmp.append(node.val)
                if node.left:
                    next.append(node.left)
                if node.right:
                    next.append(node.right)
            result.append(tmp)
            current = next
            next = []
        return result[::-1]
