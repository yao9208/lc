# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
#class NestedInteger(object):
#    def isInteger(self):
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        :rtype bool
#        """
#
#    def getInteger(self):
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        :rtype int
#        """
#
#    def getList(self):
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        :rtype List[NestedInteger]
#        """

from collections import deque
class Solution(object):
    def depthSumInverse(self, nestedList):
        """
        :type nestedList: List[NestedInteger]
        :rtype: int
        """
        queue = deque()
        result = 0
        for l in nestedList:
            queue.append(l)
            prev = 0
        while len(queue)!=0:
            cur = 0
            size = len(queue)
            for i in range(size):
                node = queue.popleft()
                if node.isInteger():
                    cur += node.getInteger()
                else:
                    tmplist = node.getList()
                    for l in tmplist:
                        queue.append(l)
            prev += cur
            result += prev
        return result
