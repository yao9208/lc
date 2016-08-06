# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root:
            return True
        return self.mirror(root.left, root.right)

    def mirror(self, p, q):
        if not p and not q:
            return True
        if not p or not q:
            return False
        else:
            return p.val == q.val and self.mirror(p.left, q.right) and self.mirror(p.right, q.left)


#iterative
class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        stack = []
        if not root:
            return True
        if not root.left or not root.right:
            return root.left==root.right
        stack = [root.left, root.right]
        while len(stack)!=0:
            right, left = stack.pop(), stack.pop()
            if left.val!=right.val:
                return False
            if right.right:
                if not left.left:
                    return False
                stack.append(left.left)
                stack.append(right.right)
            elif left.left:
                return False

            if right.left:
                if not left.right:
                    return False
                stack.append(left.right)
                stack.append(right.left)
            elif left.right:
                return False
        return True
