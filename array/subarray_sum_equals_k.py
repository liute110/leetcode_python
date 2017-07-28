#coding=utf-8

class Solution(object):
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """

        res = 0
        sum_num = 0
        res_dict = {}
        res_dict[0] = 1
        for i in nums:
        	sum_num += i 
        	if sum_num - k in  res_dict:
        		res += res_dict[sum_num - k]
        	if sum_num in res_dict:
        		res_dict[sum_num] += 1
        	else:
        		res_dict[sum_num] = 1
        return res

print Solution().subarraySum([1],0)