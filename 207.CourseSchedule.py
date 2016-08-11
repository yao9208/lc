from collections import deque
class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
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
        while len(queue)!=0:
            node = queue.popleft()
            num += 1
            for i in range(numCourses):
                if matrix[node][i]==True:
                    matrix[node][i]=False
                    indegree[i]-=1
                    if indegree[i]==0:
                        queue.append(i)
        return num==numCourses
