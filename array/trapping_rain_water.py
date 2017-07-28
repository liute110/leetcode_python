class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        if len(height) <= 1: return 0
        res = 0
        maxl = [0 for i in range(len(height))]
        maxr = [0 for i in range(len(height))]
        maxl[0] = height[0]
        maxr[-1] = height[-1]
        for i in range(1,len(height)):
        	if maxl[i-1] < height[i]: maxl[i] = height[i]
        	else: maxl[i] = maxl[i-1]
        for i in range(len(height)-2,-1,-1):
        	if maxr[i+1] < height[i]: maxr[i] = height[i]
        	else: maxr[i] = maxr[i+1]
        for i in range(len(height)-1):
        	tmp = min(maxl[i],maxr[i])
        	if tmp > height[i]:
        		res += (tmp - height[i])
        return res

s = Solution()
nums = [0,1,0,2,1,0,1,3,2,1,2,1]
s.trap(nums)
