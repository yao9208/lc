# Definition for singly-linked list with a random pointer.
# class RandomListNode(object):
#     def __init__(self, x):
#         self.label = x
#         self.next = None
#         self.random = None

class Solution(object):
    def copyRandomList(self, head):
        """
        :type head: RandomListNode
        :rtype: RandomListNode
        """
        dic = {}
        p = head
        dummy = RandomListNode(0)
        q = dummy
        while p:
            node = RandomListNode(p.label)
            dic[p] = node
            q.next = node
            p, q = p.next, q.next
        p = head
        while p:
            if p.random:
                dic[p].random = dic[p.random]
            p = p.next
        return dummy.next



# Definition for singly-linked list with a random pointer.
# class RandomListNode(object):
#     def __init__(self, x):
#         self.label = x
#         self.next = None
#         self.random = None

class Solution(object):
    def copyRandomList(self, head):
        """
        :type head: RandomListNode
        :rtype: RandomListNode
        """
        p = head
        if not head:
            return None
        while p:
            node = RandomListNode(p.label)
            q = p.next
            p.next = node
            node.next = q
            p = q
        p = head
        while p:
            if p.random:
                p.next.random = p.random.next
            p = p.next.next
        newhead = head.next
        q = newhead
        p = head
        while p:
            p.next = q.next
            if q.next:
                q.next = q.next.next
                q = q.next
            p = p.next
        return newhead
