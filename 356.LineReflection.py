class Solution(object):
    def isReflected(self, points):
        """
        :type points: List[List[int]]
        :rtype: bool
        """
        dic = set()
        maxX, minX = -sys.maxint, sys.maxint
        for point in points:
            maxX = max(maxX, point[0])
            minX = min(minX, point[0])
            key = (point[0], point[1])
            dic.add(key)
        sum = maxX+minX
        for point in points:
            if (sum - point[0], point[1]) not in dic:
                return False
        return True
