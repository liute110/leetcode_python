class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        return self.sub_search(nums,0,len(nums)-1,target)

    def sub_search(self,nums,low,high,target):
    	'''
    	if low == high:
    		if target > nums[low]:return low + 1
    		return low
    	'''
    	middle = (low + high)/2
    	if nums[middle] == target:
    		return middle 
    	elif target > nums[middle]:
    		if middle == len(nums) - 1:return len(nums)
    		if target < nums[middle+1]:return middle + 1
    		return self.sub_search(nums,middle+1,high,target)
    	else:
    		if target > nums[middle-1]:return middle
    		if middle == 0:return 0
    		return self.sub_search(nums,low,middle-1,target)

print Solution().searchInsert([1,3,5,6],5)
print Solution().searchInsert([1,3,5,6],2)
print Solution().searchInsert([1,3,5,6],7)
print Solution().searchInsert([1,3,5,6],0)
print Solution().searchInsert([1],0)