# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        dummy = ListNode(0)
        dummy.next = head
        prev = dummy
        p, q, r = head, None, None
        while p and p.next:
            q = p.next
            r = q.next
            prev.next = q
            q.next = p
            p.next = r
            prev = p
            p = r
        return dummy.next
