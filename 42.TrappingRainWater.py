class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        left, right = 0, 0
        start, end = 0, len(height)-1
        result = 0
        while start <= end:
            if left<right:
                if height[start]>=left:
                    left = height[start]
                else:
                    result += left - height[start]
                start += 1
            else:
                if height[end]>=right:
                    right = height[end]
                else:
                    result += right - height[end]
                end -= 1
        return result
