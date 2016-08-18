from collections import defaultdict
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        dic = defaultdict(list)
        for i in range(len(nums)):
            dic[nums[i]].append(i)
        for n in dic:
            if 2*n==target and len(dic[n])>1:
                return [dic[n][0], dic[n][1]]
            elif target-n in dic:
                return [dic[n][0], dic[target-n][0]]
        return None
