from collections import deque
class Solution(object):
    def maxSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        queue = deque()
        res = []
        for i in range(len(nums)):
            while len(queue)>0 and nums[i]>nums[queue[-1]]:
                queue.pop()
            while len(queue)>0 and queue[0]<i-k+1:
                queue.popleft()
            queue.append(i)
            if i>=k-1:
                res.append(nums[queue[0]])
        return res
