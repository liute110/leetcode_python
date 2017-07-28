class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if len(prices) <= 1:
        	return 0
        res = 0
        for i in range(0,len(prices)-1):
        	if prices[i] < prices[i+1]:
        		res += prices[i+1] - prices[i]
        return res

print Solution().maxProfit([2,1,2,0,1])

