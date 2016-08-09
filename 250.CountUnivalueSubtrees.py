class Solution(object):
    num = 0
    def countUnivalSubtrees(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.helper(root)
        return self.num

    def helper(self, root):
        if not root:
            return True
        left = self.helper(root.left)
        right = self.helper(root.right)
        if not left or not right:
            return False
        if root.left and root.left.val != root.val:
            return False
        if root.right and root.right.val != root.val:
            return False
        self.num+=1
        return True
