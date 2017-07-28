#coding=utf-8
class Solution(object):
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = [[]]
        elem = []
        nums.sort()
        self.sub(0,nums,res,elem)
        return res

    def sub(self,start,nums,res,elem):
    	flag = 0
    	for i in range(start,len(nums)):
    		if i>0 and  flag and nums[i]==nums[i-1]: continue
    		elem.append(nums[i])
    		res.append(elem[:])
    		flag = 1
    		self.sub(i+1,nums,res,elem)
    		elem.pop()

nums = [1,2,1,2,2]
print Solution().subsetsWithDup(nums)


        