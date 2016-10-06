# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def sortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head is None or head.next is None:
            return head
        slow, fast = head, head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        part2 = slow.next
        slow.next = None
        return self.merge(self.sortList(head), self.sortList(part2))

    def merge(self, p, q):
        dummy = ListNode(0)
        d = dummy
        while p and q:
            if p.val<q.val:
                d.next = p
                p = p.next
            else:
                d.next = q
                q = q.next
            d = d.next
        if p:
            d.next = p
        elif q:
            d.next = q
        return dummy.next
