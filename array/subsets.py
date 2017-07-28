class Solution(object):
    def subsets(self, nums):
        res = [[]]
        index_n = len(nums)
        for i in range(index_n):
        	index_r = len(res)
        	for j in range(index_r):
        		if res[j]: res.append(res[j] + [nums[i]])
        	res.append([nums[i]])
        return res
        		


print Solution().subsets([1,2,3])