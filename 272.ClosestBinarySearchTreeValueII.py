# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from collections import deque
class Solution(object):
    def closestKValues(self, root, target, k):
        """
        :type root: TreeNode
        :type target: float
        :type k: int
        :rtype: List[int]
        """
        small = deque()
        larger = deque()
        self.traverse(root, False, target, k, small)
        self.traverse(root, True, target, k, larger)
        result = []
        while k>0:
            if len(small)==0 and len(larger)==0:
                break
            if len(small)==0:
                result.append(larger.pop())
            elif len(larger)==0:
                result.append(small.pop())
            elif abs(larger[-1]-target)<abs(small[-1]-target):
                result.append(larger.pop())
            else:
                result.append(small.pop())
            k-=1
        return result

    def traverse(self, root, reverse, target, k, queue):
        if not root:
            return
        if reverse:
            self.traverse(root.right, reverse, target, k, queue)
        else:
            self.traverse(root.left, reverse, target, k, queue)
        if not reverse and root.val>target or reverse and root.val<=target:
            return
        queue.append(root.val)
        if len(queue)>k:
            queue.popleft()
        if reverse:
            self.traverse(root.left, reverse, target, k, queue)
        else:
            self.traverse(root.right, reverse, target, k, queue)
