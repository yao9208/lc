# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        result = []
        if not root:
            return result
        cur = [root]
        flag = True
        while len(cur)!=0:
            next = []
            curresult = []
            while len(cur)!=0:
                node = cur.pop()
                curresult.append(node.val)
                if not flag:
                    if node.right:
                        next.append(node.right)
                    if node.left:
                        next.append(node.left)
                else:
                    if node.left:
                        next.append(node.left)
                    if node.right:
                        next.append(node.right)
            result.append(curresult)
            cur = next
            flag = not flag
        return result
