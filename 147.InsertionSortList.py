# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def insertionSortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        dummy = ListNode(0)
        while head:
            next = head.next
            p = dummy
            while p.next:
                if head.val<p.next.val:
                    q = p.next
                    p.next = head
                    head.next = q
                    break
                p = p.next
            if not p.next:
                p.next = head
                head.next = None
            head = next
        return dummy.next

#Actually got TLE with python, same algo with java passed.
