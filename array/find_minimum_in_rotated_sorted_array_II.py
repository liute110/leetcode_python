#coding=utf-8
class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        low = 0
        high = len(nums) - 1
        while low < high:
        	if low == high: return nums[low]
        	mid = (low+high)/2
        	if nums[mid] > nums[high]: low = mid + 1
        	elif nums[mid] == nums[high]: high -= 1
        	else: high = mid
        return nums[low]
        