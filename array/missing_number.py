#coding=utf-8
class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        sum_nums = 0
        for i in nums:
        	sum_nums += i 
        return len(nums)*(len(nums)+1)/2 -sum_nums

print Solution().missingNumber([0])