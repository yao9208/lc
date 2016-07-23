class Solution(object):
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        start, end = 0, len(citations)-1
        if len(citations)==0:
            return 0
        while start <= end:
            mid = start + (end-start)/2
            if citations[mid]<len(citations)-mid:
                start = mid + 1
            else:
                end = mid - 1
        return len(citations)-start
