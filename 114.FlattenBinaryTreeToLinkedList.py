class Solution(object):
    def flatten(self, root):
        """
        :type root: TreeNode
        :rtype: void Do not return anything, modify root in-place instead.
        """
        if not root:
            return root
        stack = [root]
        parent = TreeNode(0)
        while len(stack)!=0:
            node = stack.pop()
            parent.right = node
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)
            node.left = None
            parent = node

#https://discuss.leetcode.com/topic/11444/my-short-post-order-traversal-java-solution-for-share/2
