class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        res = 0
        low = 0
        high = len(height)-1
        while low < high:
        	res = max(res,min(height[low],height[high])*(high-low))
        	if height[low] > height[high]:
        		index = low 
        		while index < high and height[index] <= height[low]:
        			index += 1
        	else:
        		index = high 
        		while index > low and height[index] <= height[high]:
        			index -= 1
        return res