# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        p, q = headA, headB
        if not q or not p: return None
        while p and q and p!=q:
            p = p.next
            q = q.next
            if p==q:
                return p
            if not p:
                p = headB
            if not q:
                q = headA
        return p
