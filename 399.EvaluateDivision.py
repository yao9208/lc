from collections import defaultdict
class Solution(object):
    def calcEquation(self, equations, values, query):
        """
        :type equations: List[List[str]]
        :type values: List[float]
        :type query: List[List[str]]
        :rtype: List[float]
        """
        dic = self.makeDic(equations, values)
        result = []
        for q in query:
            visited = set()
            res = self.evaluate(q[0], q[1], dic, visited)
            res = -1.0 if res is None else res
            result.append(res)
        return result

    def makeDic(self, equations, values):
        n = len(equations)
        dic = defaultdict(dict)
        for i in range(n):
            dic[equations[i][0]][equations[i][1]] = values[i]
            dic[equations[i][1]][equations[i][0]] = 1.0/values[i]
        return dic

    def evaluate(self, num, denom, dic, visited):
        dupkey = num+":"+denom
        if num not in dic or denom not in dic:
            return None
        if num==denom:
            return 1.0
        if dupkey in visited:
            return None
        for key in dic[num]:
            visited.add(dupkey)
            res = self.evaluate(key, denom, dic, visited)
            if res:
                return res * dic[num][key]
            visited.remove(dupkey)
        return None
