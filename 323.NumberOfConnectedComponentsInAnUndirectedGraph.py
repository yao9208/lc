from collections import defaultdict
class Solution(object):
    def countComponents(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: int
        """
        dic = defaultdict(list)
        for edge in edges:
            p,q = edge[0], edge[1]
            dic[p].append(q)
            dic[q].append(p)
        sign = [1]*n
        visited = [False]*n
        for i in range(n):
            if sign[i]==1:
                self.search(i, dic, sign, visited)
        return sum(sign)

    def search(self, node, dic, sign, visited):
        if visited[node]:
            return
        visited[node]=True
        for p in dic[node]:
            if visited[p]:
                continue
            sign[p] = 0
            self.search(p, dic, sign, visited)
