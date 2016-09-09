class Solution(object):
    def minTotalDistance(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        m, n = len(grid), len(grid[0])
        row, col = [], []
        for i in range(m):
            for j in range(n):
                if grid[i][j]==1:
                    row.append(i)
        for j in range(n):
            for i in range(m):
                if grid[i][j]==1:
                    col.append(j)
        return self.minDis(row)+self.minDis(col)

    def minDis(self, arr):
        i, j = 0, len(arr)-1
        res = 0
        while i<j:
            res += arr[j]-arr[i]
            i+=1
            j-=1
        return res
