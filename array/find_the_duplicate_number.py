#coding=utf-8

class Solution(object):
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        for i in range(len(nums)):
        	if nums[abs(nums[i])] < 0:
        		return abs(nums[i])
        	nums[abs(nums[i])] *= -1

print Solution().findDuplicate([1,1])
        		