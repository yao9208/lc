class Solution(object):
    def wallsAndGates(self, rooms):
        """
        :type rooms: List[List[int]]
        :rtype: void Do not return anything, modify rooms in-place instead.
        """
        m = len(rooms)
        if m==0:
            return
        n = len(rooms[0])
        for i in range(m):
            for j in range(n):
                if rooms[i][j]==0:
                    self.dfs(rooms, i, j, 0)

    def dfs(self, rooms, x, y, cur):
        dir = [(0,1),(0,-1),(1,0),(-1,0)]
        if x<0 or x>=len(rooms) or y<0 or y>=len(rooms[0]) or rooms[x][y]==-1:
            return
        if rooms[x][y]==0 and cur!=0:
            return
        elif rooms[x][y]<cur:
            return
        rooms[x][y]=cur
        for d in dir:
            self.dfs(rooms, x+d[0], y+d[1], cur+1)
            
