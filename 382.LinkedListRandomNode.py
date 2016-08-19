# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):

    def __init__(self, head):
        """
        @param head The linked list's head.
        Note that the head is guaranteed to be not null, so it contains at least one node.
        :type head: ListNode
        """
        self.n = 0
        p = head
        while p:
            self.n+=1
            p = p.next
        self.ptr = head
        self.head = head


    def getRandom(self):
        """
        Returns a random node's value.
        :rtype: int
        """
        step = random.randint(0, self.n)
        for i in range(step):
            self.ptr = self.ptr.next
            if not self.ptr:
                self.ptr = self.head
        return self.ptr.val



# Your Solution object will be instantiated and called as such:
# obj = Solution(head)
# param_1 = obj.getRandom()
