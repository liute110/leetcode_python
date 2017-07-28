#coding=utf-8
class Solution(object):
    def matrixReshape(self, nums, r, c):
        """
        :type nums: List[List[int]]
        :type r: int
        :type c: int
        :rtype: List[List[int]]
        """

        if r*c > len(nums)*len(nums[0]):
        	return nums
        result = []
        for i in nums:
        	for j in i:
        		if not result:
        			result.append([j])
        			continue
        		if len(result[-1]) < c:
        			result[-1].append(j)
        		else:
        			result.append([j])
        return result

nums = [[1,2],[3,4]]
print Solution().matrixReshape(nums,2,2)


