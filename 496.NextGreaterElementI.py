class Solution(object):
    def nextGreaterElement(self, findNums, nums):
        """
        :type findNums: List[int]
        :type nums: List[int]
        :rtype: List[int]
        """
        dic = {}
        for i in range(len(nums)):
            dic[nums[i]] = i
        result = []
        for n in findNums:
            index = dic[n]
            i = index+1
            while i<len(nums):
                if(nums[i]>n):
                    result.append(nums[i])
                    break
                i+=1
            if i==len(nums):
                result.append(-1)

        return result
