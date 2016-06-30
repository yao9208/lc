# Definition for a  binary tree node
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

from collections import deque
class BSTIterator(object):
    def __init__(self, root):
        """
        :type root: TreeNode
        """
        self.stack = deque()
        self.pushAll(root)


    def hasNext(self):
        """
        :rtype: bool
        """
        return self.stack


    def next(self):
        """
        :rtype: int
        """
        tmp = self.stack.pop()
        self.pushAll(tmp.right)
        return tmp.val

    def pushAll(self, node):
        while node:
            self.stack.append(node)
            node = node.left


# Your BSTIterator will be called like this:
# i, v = BSTIterator(root), []
# while i.hasNext(): v.append(i.next())
