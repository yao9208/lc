class Solution(object):
    def validTree(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: bool
        """
        dic = {}
        for i in range(n):
            dic[i] = set()
        for e in edges:
            dic[e[0]].add(e[1])
            dic[e[1]].add(e[0])
        stack = []
        visited = [False]*n
        stack.append(0)
        while len(stack)>0:
            node = stack.pop()
            if visited[node]:
                return False
            visited[node] = True
            for neighbor in dic[node]:
                dic[neighbor].remove(node)
                stack.append(neighbor)
        for flag in visited:
            if not flag:
                return False
        return True


class Solution(object):
    def validTree(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: bool
        """
        p = [i for i in range(n)]
        for e in edges:
            x = self.find(p, e[0])
            y = self.find(p, e[1])
            if x==y:
                return False
            p[y] = x
        return len(edges)==n-1

    def find(self, p, i):
        if p[i]==i:
            return i
        return self.find(p, p[i])
