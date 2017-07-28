#coding=utf-8
class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        maxnum = 0
        curmax = 0
        for i in nums:
        	if i <> 0:
        		curmax += 1
        	else:
        		curmax = 0
        	if curmax > maxnum:
        		maxnum = curmax
        return maxnum

print Solution().findMaxConsecutiveOnes([1,1,0,1,1,1])
