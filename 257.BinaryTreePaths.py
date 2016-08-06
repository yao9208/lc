# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param {TreeNode} root
    # @return {string[]}
    def binaryTreePaths(self, root):
        result = []
        if not root:
            return result
        l = ""
        self.find(root, l, result)
        return result

    def find(self, node, l, result):
        if not node:
            return
        l += str(node.val)
        if not node.left and not node.right:
            result.append(l)
        else:
            l += "->"
            self.find(node.left, l, result)
            self.find(node.right, l, result)
