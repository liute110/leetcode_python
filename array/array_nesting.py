#coding=utf-8


class Solution(object):
    def arrayNesting(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        def search(index):
        	cnt = 0
        	while nums[index] >= 0:
        		cnt += 1
        		
        		next = nums[index]
        		nums[index] = -1
        		index = next
        	return cnt

        ans = 0
        for x in range(len(nums)):
        	if nums[x] >= 0:
        		ans = max(ans,search(x))
        return ans

print Solution().arrayNesting([0,2,1])