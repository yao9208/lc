class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        if not nums:
            return []
        can1, can2 = 0, 1
        count1, count2 = 0, 0
        for n in nums:
            if n==can1:
                count1+=1
            elif n==can2:
                count2+=1
            elif count1==0:
                can1, count1 = n, 1
            elif count2==0:
                can2, count2 = n, 1
            else:
                count1, count2 = count1-1, count2-1
        return [n for n in (can1, can2) if nums.count(n)>len(nums)//3]
