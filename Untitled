# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        carry = 0
        length1 = self.length(l1)
        length2 = self.length(l2)
        result = ListNode(0)
        p=result
        if length2>length1:
            l2, l1 = l1, l2
        while l1:
            if not l2:
                num2 = 0
            else:
                num2 = l2.val
            num = l1.val + num2 + carry
            carry = num//10
            num = num % 10
            p.next = ListNode(num)
            p = p.next
            l1 = l1.next
            if l2:
                l2 = l2.next
        if carry!=0:
            p.next = ListNode(carry)
        return result.next


    def length(self, l):
        result = 0
        while l:
            result += 1
            l = l.next
        return result
