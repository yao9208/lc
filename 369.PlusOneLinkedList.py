# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def plusOne(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        dummy = ListNode(0)
        dummy.next = head
        p, q = dummy, dummy
        while q.next:
            q = q.next
            if q.val!=9:
                p = q
        if q.val!=9:
            q.val+=1
        else:
            p.val += 1
            while p.next:
                p = p.next
                p.val = 0
        if dummy.val==0:
            return dummy.next
        return dummy
