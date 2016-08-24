class Solution(object):
    def compareVersion(self, version1, version2):
        """
        :type version1: str
        :type version2: str
        :rtype: int
        """
        v1 = version1.split('.')
        v2 = version2.split('.')
        n = max(len(v1), len(v2))
        for i in range(n):
            num1 = 0 if i>=len(v1) else int(v1[i])
            num2 = 0 if i>=len(v2) else int(v2[i])
            if num1>num2:
                return 1
            elif num1<num2:
                return -1
        return 0
