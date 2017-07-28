#coding=utf-8

class Solution(object):
	def find_disappeared_numbers(self,nums):
		'''
		:type nums: List[int]
        :rtype: List[int]
		'''
		result = []
		for i in range(len(nums)):
			index = abs(nums[i])
			if nums[index-1] > 0:
				nums[index-1] = nums[index-1]*(-1) 
		for i,v in enumerate(nums):
			if v > 0:
				result.append(i+1) 
		return result


print Solution().find_disappeared_numbers([2,2])