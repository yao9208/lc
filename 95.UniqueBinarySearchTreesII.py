# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def generateTrees(self, n):
        """
        :type n: int
        :rtype: List[TreeNode]
        """
        dic = {}
        dic[0] = [None]
        if n==0: return []
        for i in range(1, n+1):
            dic[i] = []
            for j in range(i):
                left = dic[j]
                right = dic[i-1-j]
                for l in left:
                    for r in right:
                        clone = self.addBase(r, j+1)
                        root = TreeNode(j+1)
                        root.left = l
                        root.right = clone
                        dic[i].append(root)
        return dic[n]

    def addBase(self, node, val):
        if not node:
            return None
        clone = TreeNode(node.val+val)
        clone.left = self.addBase(node.left, val)
        clone.right = self.addBase(node.right, val)
        return clone
        '''
        stack = []
        stack.append(node)
        while len(stack)!=0:
            cur = stack.pop()
            cur.val += val
            if cur.right:
                stack.append(cur.right)
            if cur.left:
                stack.append(cur.left)
        return node
        '''
        
