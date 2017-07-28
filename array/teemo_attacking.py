#coding=utf-8

class Solution(object):
    def findPoisonedDuration(self, timeSeries, duration):
        """
        :type timeSeries: List[int]
        :type duration: int
        :rtype: int
        """
        if not timeSeries:
        	return 0
        result = 0
        pre = timeSeries[0]
        for i in range(1,len(timeSeries)):
        	if timeSeries[i] - pre < duration:
        		result += timeSeries[i] - pre
        	else:
        		result += duration
        	pre = timeSeries[i]
        return result + duration


print Solution().findPoisonedDuration([1,2], 2) 