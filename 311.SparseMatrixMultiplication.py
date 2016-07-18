class Solution(object):
    def multiply(self, A, B):
        """
        :type A: List[List[int]]
        :type B: List[List[int]]
        :rtype: List[List[int]]
        """
        m = len(A)
        n = len(B[0])
        dicA, dicB = {}, {}
        result = [[0 for x in range(n)] for x in range(m)]
        for i in range(len(A)):
            dicA[i] = {}
            for j in range(len(A[0])):
                if A[i][j]!=0:
                    dicA[i][j] = A[i][j]
        for j in range(len(B[0])):
            dicB[j] = {}
            for i in range(len(B)):
                if B[i][j]!=0:
                    dicB[j][i] = B[i][j]
        for i in range(m):
            for j in range(n):
                if len(dicA[i])!=0 and len(dicB[j])!=0:
                    tmp = 0
                    for p in dicA[i]:
                        if p in dicB[j]:
                           tmp += dicA[i][p] * dicB[j][p]
                    result[i][j] = tmp
        return result

#one dic is enough
