class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        result = ['']*numRows
        flag = False
        i = 0
        n = len(s)
        while i<n:
            p = 0
            while i<n and p<numRows:
                result[p] += s[i]
                i+=1
                p+=1
            p = numRows-2
            while i<n and p>0:
                result[p]+= s[i]
                i+=1
                p-=1
        return ''.join(result)
