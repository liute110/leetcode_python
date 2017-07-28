#coding=utf-8

'''
class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        if m < 1 or n < 1:
        	return 0
        res = 0
        res = self.sub_path(m,n)
        return res

    def sub_path(self,m,n):
    	res = 0
    	if m == 1 and n == 1:
    		res = 1
    	elif m == 1:
    		res = self.sub_path(m,n-1)
    	elif n == 1:
    		res =  self.sub_path(m-1,n)
    	else:
    		res = self.sub_path(m-1,n) + self.sub_path(m,n-1)
    	return res 
'''

class Solution(object):
	def uniquePaths(self, m, n):
		if m < 1 or n < 1:
			return 0
		f = [[0 for i in range(0,n)] for j in range(0,m)]
		for i in range(m):
			for j in range(n):
				if i == 0 and j == 0:
					f[i][i] = 1
				elif i == 0:
					f[i][j] = f[i][j-1]
				elif j == 0:
					f[i][j] = f[i-1][j]
				else:
					f[i][j] = f[i-1][j] + f[i][j-1]
		return f[m-1][n-1]




print Solution().uniquePaths(2,3)