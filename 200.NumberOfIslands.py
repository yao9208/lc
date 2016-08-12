class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        count = 0
        m = len(grid)
        if m==0:
            return 0
        n = len(grid[0])
        for i in range(m):
            for j in range(n):
                if self.find(grid, i, j)==True:
                    count += 1
        return count

    def find(self, grid, x, y):
        m = len(grid)
        n = len(grid[0])
        if x<0 or x>=m or y<0 or y>=n:
            return False
        if grid[x][y]=='.' or grid[x][y]=='0':
            return False
        if grid[x][y]=='1':
            grid[x][y]='.'
            #self.count += 1
            self.find(grid, x+1, y)
            self.find(grid, x-1, y)
            self.find(grid, x, y+1)
            self.find(grid, x, y-1)
        return True
