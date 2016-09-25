# Definition for binary tree with next pointer.
# class TreeLinkNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#         self.next = None

class Solution:
    # @param root, a tree link node
    # @return nothing
    def connect(self, root):
        cur = root
        while cur:
            nextlevel, p = None, None
            while cur:
                if cur.left:
                    if not nextlevel:
                        nextlevel = cur.left
                    else:
                        p.next = cur.left
                    p = cur.left
                if cur.right:
                    if not nextlevel:
                        nextlevel = cur.right
                    else:
                        p.next = cur.right
                    p = cur.right
                cur = cur.next
            cur = nextlevel
