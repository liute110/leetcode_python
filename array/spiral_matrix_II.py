#coding=utf-8
class Solution(object):
    def generateMatrix(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        if n <= 0: return [[]]
        counter = 1
        top = 0
        bottom = n - 1
        left = 0
        right = n - 1
        res = [[0 for i in range(n)] for j in range(n)]
        while True:
        	#上边
        	for i in range(left,right+1):
        		res[top][i] = counter
        		counter += 1
        	if top == bottom: break
        	top += 1

        	#右边
        	for i in range(top,bottom+1): 
        		res[i][right] = counter
        		counter += 1
        	if right == left: break 
        	right -= 1

        	#下边
        	for i in range(right,left-1,-1):
        		res[bottom][i] = counter
        		counter += 1
        	if top == bottom: break 
        	bottom -= 1

        	#左边
        	print bottom,top
        	for i in range(bottom,top-1,-1): 
        		res[i][left] = counter
        		counter += 1  	
        	if left == right: break
        	left += 1
        return res

print Solution().generateMatrix(1)
