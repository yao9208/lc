class Solution(object):
    result = 0
    def longestConsecutive(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        self.helper(root, root.val-1, 0)
        return self.result

    def helper(self, root, prev, length):
        if not root:
            return
        if root.val!=prev+1:
            if root.left:
                self.helper(root.left, root.val, 1)
            if root.right:
                self.helper(root.right, root.val, 1)
        else:
            length+=1
            self.result = max(self.result, length)
            self.helper(root.left, root.val, length)
            self.helper(root.right, root.val, length)
