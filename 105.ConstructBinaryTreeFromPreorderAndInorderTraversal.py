class Solution(object):
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        return self.build(preorder, 0, len(preorder)-1, inorder, 0, len(inorder)-1)

    def build(self, preorder, prestart, preend, inorder, instart, inend):
        if prestart<0 or preend>=len(preorder) or instart<0 or inend>= len(inorder) or prestart>preend or instart>inend:
            return None
        root = TreeNode(preorder[prestart])
        ind = instart
        while inorder[ind]!=root.val and ind<=inend:
            ind+=1
        left = ind-instart
        root.left = self.build(preorder, prestart+1, prestart+left, inorder, instart, ind-1)
        root.right = self.build(preorder, prestart+left+1, preend, inorder, ind+1, inend)
