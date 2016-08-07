class Solution(object):
    def findLeaves(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        result = []
        self.height(root, result)
        return result

    def height(self, root, result):
        if not root:
            return -1
        left = 1+self.height(root.left, result)
        right = 1+self.height(root.right, result)
        h = max(left, right)
        if len(result)<=h:
            result.append([root.val])
        else:
            result[h].append(root.val)
        return h
