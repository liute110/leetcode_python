#coding=utf-8

class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        result = []
    	pre = 1
    	for i in nums:
    		result.append(pre)
    		pre *= i
    	pre = 1
    	for i in range(len(nums)-1,-1,-1):
    		result[i] *= pre
    		pre *= nums[i]
    	return result


print Solution().productExceptSelf([1,2,3,4])