# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseKGroup(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if not head or k==1:
            return head
        p = head
        for i in range(k-1):
            p = p.next
            if not p:
                return head
        tail = self.reverseKGroup(p.next, k)
        prev, cur = None, head
        count = k   #IMPORTANT
        while cur and count>0:
            count-=1
            next = cur.next
            cur.next = prev
            prev = cur
            cur = next
        head.next = tail
        return prev
