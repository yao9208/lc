# Definition for an interval.
# class Interval(object):
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution(object):
    def insert(self, intervals, newInterval):
        """
        :type intervals: List[Interval]
        :type newInterval: Interval
        :rtype: List[Interval]
        """
        result = []
        i = 0
        n = len(intervals)
        while i<n and intervals[i].end<newInterval.start:
            result.append(intervals[i])
            i+=1
        while i<n and newInterval.end>=intervals[i].start:
            newInterval = Interval(min(intervals[i].start, newInterval.start), max(intervals[i].end, newInterval.end))
            i+=1
        result.append(newInterval)
        while i<n:
            result.append(intervals[i])
            i+=1
        return result
