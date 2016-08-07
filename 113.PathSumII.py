# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: List[List[int]]
        """
        result = []
        self.helper(root, result, [], sum)
        return result

    def helper(self, root, result, curlist, target):
        if not root:
            return
        l = curlist[:]
        l.append(root.val)
        if not root.left and not root.right and root.val==target:
            result.append(l)
            return
        if root.left:
            self.helper(root.left, result, l, target-root.val)
        if root.right:
            self.helper(root.right, result, l , target-root.val)
        
