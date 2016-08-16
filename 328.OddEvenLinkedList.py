# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def oddEvenList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        oddp, evenp = ListNode(0), ListNode(0)
        odd, even = oddp, evenp
        while head:
            odd.next = head
            even.next = head.next
            odd = odd.next
            even = even.next
            if even:
                head = head.next.next
            else:
                break
        odd.next = evenp.next
        return oddp.next
