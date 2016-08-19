class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        start, end = 0, len(height)-1
        maxarea = 0
        while start < end:
            low, high = height[start], height[end]
            area = min(low, high) * (end-start)
            maxarea = max(maxarea, area)
            if low<high:
                while start<end and height[start]<=low:
                    start+=1
            else:
                while start<end and height[end]<=high:
                    end-=1
        return maxarea
