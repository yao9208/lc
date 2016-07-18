class Solution(object):
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        length = len(citations)
        freq = [0 for x in range(length+1)]
        for c in citations:
            if c>length:
                freq[length]+=1
            else:
                freq[c]+=1
        h = 0
        for i in range(length, -1, -1):
            h += freq[i]
            if h>=i:
                return i
        return 0
