class Solution(object):
    def generateMatrix(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        result = [[0 for x in range(0, n)] for x in range(0, n)]
        layer = int(n/2)
        num = 1
        for k in range(0, layer):
            for i in range(k, n-1-k):
                result[k][i] = num
                num += 1
            for i in range(k, n-1-k):
                result[i][n-1-k]= num
                num += 1
            for i in range(n-1-k, k, -1):
                result[n-1-k][i] = num
                num += 1
            for i in range(n-1-k, k, -1):
                result[i][k] = num
                num += 1
        if n%2==1:
            result[layer][layer] = num
        return result
