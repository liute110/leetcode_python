#coding=utf-8

class Solution(object):
	def findDuplicates(self, nums):
		result = []
		for i in range(len(nums)):
			if nums[abs(nums[i])-1] < 0:
				result.append(abs(nums[i]))
			else:
				nums[abs(nums[i])-1] = nums[abs(nums[i])-1]*(-1)
		return result

print Solution().findDuplicates([2,2])