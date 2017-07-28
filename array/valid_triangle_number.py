class Solution(object):
    def triangleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        #if len(nums) <= 2: return 0
        nums.sort()
        res = 0
        for i in range(len(nums)-2):
        	if nums[i] == 0: continue
        	k = i + 2;
        	for j in range(i+1,len(nums)-1):
        		while k < len(nums) and nums[k] < nums[i] + nums[j]:
        			k += 1
        		res += k-j-1
        return res 

print Solution().triangleNumber([2,2,3,4])
