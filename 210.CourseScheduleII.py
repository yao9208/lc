from collections import deque
class Solution(object):
    def findOrder(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: List[int]
        """
        matrix = [[False]*numCourses for x in range(numCourses)]
        indegree = [0]*numCourses
        for item in prerequisites:
            course = item[0]
            pre = item[1]
            if not matrix[pre][course]:
                matrix[pre][course]=True
                indegree[course]+=1
        queue = deque()
        for i in range(numCourses):
            if indegree[i]==0:
                queue.append(i)
        num = 0
        result = []
        while len(queue)!=0:
            node = queue.popleft()
            result.append(node)
            num += 1
            for i in range(numCourses):
                if matrix[node][i]==True:
                    matrix[node][i]=False
                    indegree[i]-=1
                    if indegree[i]==0:
                        queue.append(i)
        if num!=numCourses:
            return []
        return result
