class Solution(object):
    def buildTree(self, inorder, postorder):
        """
        :type inorder: List[int]
        :type postorder: List[int]
        :rtype: TreeNode
        """
        return self.build(inorder, 0, len(inorder)-1, postorder, 0, len(postorder)-1)

    def build(self, inorder, instart, inend, postorder, poststart, postend):
        if instart>inend or poststart>postend:
            return None
        root = TreeNode(postorder[postend])
        i = instart
        while inorder[i]!=postorder[postend]:
            i+=1
        len = i-instart
        root.left = self.build(inorder, instart, i-1, postorder, poststart, poststart+len-1)
        root.right = self.build(inorder, i+1, inend, postorder, poststart+len, postend-1)
        return root
