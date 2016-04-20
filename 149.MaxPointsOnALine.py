# Definition for a point.
# class Point(object):
#     def __init__(self, a=0, b=0):
#         self.x = a
#         self.y = b

class Solution(object):
    def maxPoints(self, points):
        """
        :type points: List[Point]
        :rtype: int
        """
        result = 0
        if len(points)<=2:
            return len(points)
        for i in range(len(points)):
            a = points[i]
            dup = 0
            vertical = 0
            dic = {}
            for j in range(i+1, len(points)):
                b = points[j]
                if a.x == b.x:
                    if a.y == b.y:
                        dup += 1
                    else:
                        vertical += 1
                else:
                    slope = (b.y-a.y)*1.0/(b.x-a.x)
                    #default is integer division
                    if slope in dic:
                        dic[slope] += 1
                    else:
                        dic[slope] = 1
            slopemax = 0
            if len(dic)>0:
                slopemax = max(dic.values())
            tmp = max(dup + slopemax+1, dup+vertical+1)
            result = max(result, tmp)
        return result
        #pay attention to identation for python
