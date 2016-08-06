# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if root:
            root.left, root.right = root.right, root.left
            self.invertTree(root.left)
            self.invertTree(root.right)
        return root

#iterative

class Solution(object):
    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if not root:
            return root
        stack = [root]
        while len(stack)!=0:
            node = stack.pop()
            left = node.left
            node.left = node.right
            node.right = left
            if node.left:
                stack.append(node.left)
            if node.right:
                stack.append(node.right)
        return root
