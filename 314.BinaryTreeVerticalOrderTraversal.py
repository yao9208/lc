# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from collections import deque
class Solution(object):
    def verticalOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        result = []
        queue = deque()
        dic = {}
        minorder, maxorder = sys.maxint, -sys.maxint
        if not root:
            return result
        queue.append((root, 0))
        while len(queue)!=0:
            size = len(queue)
            for i in range(size):
                cur = queue.popleft()
                node = cur[0]
                order = cur[1]
                minorder = min(order, minorder)
                maxorder = max(order, maxorder)
                if node.left:
                    queue.append((node.left, order-1))
                if node.right:
                    queue.append((node.right, order+1))
                if order in dic:
                    dic[order].append(node.val)
                else:
                    dic[order] = [node.val]
        for i in range(minorder, maxorder+1):
            result.append(dic[i])
        return result
