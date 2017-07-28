#coding=utf-8
class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums: return 0
        index = 0
        isRepeated = False 
        for i in range(1,len(nums)):
            if nums[i] !=  nums[i-1]:
        	index += 1
        	nums[index] = nums[i]
        	isRepeated = False
            else:
                if not isRepeated:
                    index += 1
                    nums[index] = nums[i]
                    isRepeated = True
        
	return (index + 1 )      

nums = [1,1,1,2,2,2,3]
print Solution().removeDuplicates(nums)
