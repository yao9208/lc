class Solution(object):
    def getModifiedArray(self, length, updates):
        """
        :type length: int
        :type updates: List[List[int]]
        :rtype: List[int]
        """
        result = [0 for x in range(length)]
        for u in updates:
            val = u[2]
            end = u[1]
            start = u[0]
            result[start] += val
            if end < length-1:
                result[end+1] -= val
        sum = 0
        for i in range(length):
            sum += result[i]
            result[i] = sum
        return result
        
