# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    list = None
    def sortedListToBST(self, head):
        """
        :type head: ListNode
        :rtype: TreeNode
        """
        self.list = head
        n = self.count(head)
        return self.helper(0, n-1)

    def helper(self, start, end):
        if start>end:
            return None
        mid = start + (end-start)/2
        left = self.helper(start, mid-1)
        root = TreeNode(self.list.val)
        self.list = self.list.next
        right = self.helper(mid + 1, end)
        root.left = left
        root.right = right
        return root

    def count(self, node):
        if not node:
            return 0
        result = 0
        while node:
            result += 1
            node = node.next
        return result
