# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or not head.next:
            return head
        next = head.next
        newhead = self.reverseList(next)
        next.next = head
        head.next = None
        return newhead


class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or not head.next:
            return head
        p, q = head, head.next
        dummy = ListNode(0)
        r = None
        dummy.next = r

        while p:
            q = p.next
            dummy.next = p
            p.next = r
            r = p
            p = q
        return dummy.next

#https://discuss.leetcode.com/topic/13268/in-place-iterative-and-recursive-java-solution
