class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """ 
        return self.sun_find(nums,0,len(nums) - 1)

    def sun_find(self,nums,low ,high):
    	if high - low <= 1:
    		return min(nums[low],nums[high])
    	middle = (low + high)/2
    	if nums[middle] < nums[middle+1] and nums[middle] < nums[middle-1]:
    	    return nums[middle]
    	if nums[low] > nums[high]:
    	    if nums[low] < nums[middle]:
    		return self.sun_find(nums,middle+1,high)
    	    elif nums[low] > nums[middle]:
    		return self.sun_find(nums,low,middle-1)
	return nums[low]



print Solution().findMin([1,2])
