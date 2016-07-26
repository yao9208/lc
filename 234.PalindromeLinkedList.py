# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if not head or not head.next:
            return True
        slow, fast = head, head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        mid = slow.next
        mid = self.reverse(mid)
        while head and mid:
            if head.val != mid.val:
                return False
            head = head.next
            mid = mid.next
        return True

    def reverse(self, head):
        prev, next = None, None
        while head:
            next = head.next
            head.next = prev
            prev = head
            head = next
        return prev
