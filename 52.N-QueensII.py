class Solution(object):
    result = 0
    def totalNQueens(self, n):
        """
        :type n: int
        :rtype: int
        """
        solution = [0]*n
        self.solve(n, solution, 0)
        return self.result

    def solve(self, n, solution, row):
        if row==n:
            self.result += 1
            return
        for i in range(n):
            if self.isValid(solution, row, i):
                solution[row]=i
                self.solve(n, solution, row+1)

    def isValid(self, solution, row, x):
        for i in range(row):
            if solution[i]==x:
                return False
            if abs(solution[i]-x)==abs(i-row):
                return False
        return True
