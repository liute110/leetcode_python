class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        l0 = l1 = l2 = 0
        for i in nums:
        	if i == 0: l0 += 1
        	if i == 1: l1 += 1
        	else: l2 += 1
        for i in range(len(nums)):
        	if i < l0: nums[i] = 0
        	elif i < l0 + l1: nums[i] = 1
        	else: nums[i] = 2