# Definition for an interval.
# class Interval(object):
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[Interval]
        """
        result = []
        if not intervals or len(intervals)==0:
            return result
        intervals.sort(key=lambda x:x.start)
        i = 1
        newitem = intervals[0]
        while i<len(intervals):
            if newitem.end>=intervals[i].start:
                newitem = Interval(newitem.start, max(newitem.end, intervals[i].end))
            else:
                result.append(newitem)
                newitem = intervals[i]
            i+=1
        result.append(newitem)
        return result
            
