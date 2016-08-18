class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        if len(matrix)==0:
            return []
        m, n = len(matrix), len(matrix[0])
        rowbegin, rowend = 0, m-1
        colbegin, colend = 0, n-1
        result = []
        while rowbegin<=rowend and colbegin<=colend:
            for i in range(colbegin, colend+1):
                result.append(matrix[rowbegin][i])
            rowbegin += 1
            for i in range(rowbegin, rowend+1):
                result.append(matrix[i][colend])
            colend -= 1
            if rowend>=rowbegin:
                for i in range(colend, colbegin-1, -1):
                    result.append(matrix[rowend][i])
                rowend -= 1
            if colend>=colbegin:
                for i in range(rowend, rowbegin-1, -1):
                    result.append(matrix[i][colbegin])
                colbegin += 1
        return result


#line 20, 24
