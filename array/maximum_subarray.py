class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:return 0
        g_max = nums[0]
        l_max = nums[0]
        for i in range(1,len(nums)):
        	l_max = max(nums[i],nums[i]+l_max)
        	g_max = max(g_max,l_max)
        return g_max