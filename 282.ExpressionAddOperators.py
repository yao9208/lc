class Solution(object):
    def addOperators(self, num, target):
        """
        :type num: str
        :type target: int
        :rtype: List[str]
        """
        result = []
        self.helper(result, '', num, target, 0, 0, 0)
        return result

    def helper(self, result, cur, num, target, cum, multed, idx):
        if idx == len(num):
            if cum==target:
                result.append(cur)
            return
        for i in range(idx, len(num)):
            tmp = int(num[idx:i+1])
            if i>idx and num[idx]=='0':
                continue
            if idx==0:
                self.helper(result, cur+str(tmp), num, target, tmp, tmp, i+1)
            else:
                self.helper(result, cur+'+'+str(tmp), num, target, cum+tmp, tmp, i+1)
                self.helper(result, cur+'-'+str(tmp), num, target, cum-tmp, -tmp, i+1)
                self.helper(result, cur+'*'+str(tmp), num, target, cum-multed+multed*tmp, multed*tmp, i+1)
