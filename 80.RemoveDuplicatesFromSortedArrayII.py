class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        twice = False
        ptr = 1
        if len(nums)<=2:
            return len(nums)
        n = size = len(nums)
        for i in range(1,size):
            if nums[i]!=nums[i-1]:
                nums[ptr]=nums[i]
                twice = False
                ptr+=1
            else:
                if not twice:
                    twice = True
                    nums[ptr]=nums[i]
                    ptr+=1
                else:
                    n-=1
        return n
