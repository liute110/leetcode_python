class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        maxl = 0
        curl = 0
        dic = {}
        for i in range(len(nums)):
        	dic[nums[i]] = 0
        for i in range(len(nums)):
        	if nums[i] not in dic: continue
        	dic.pop(nums[i])
        	curl = 1
        	curn = nums[i] - 1
        	while True:
        		if curn in dic: 
        			dic.pop(curn)
        			curl += 1
        			curn -= 1
        		else:
  					break
        	curn = nums[i] + 1
        	while True:
        		if curn in dic: 
        			dic.pop(curn)
        			curl += 1
        			curn += 1
        		else:
        			break
        	maxl = max(maxl,curl)
        return maxl