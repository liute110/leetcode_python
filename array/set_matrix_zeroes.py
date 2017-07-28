class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        r = len(matrix)
        c = len(matrix[0])
        vr = [1 for i in range(r)]
        vc = [1 for i in range(c)]

        for i in range(r):
        	for j in range(c):
        		if matrix[i][j] == 0:
        			vr[i] = 0
        			vc[j] = 0

        for i in range(r):
        	if mr[i] == 0:
        		for j in range(c):
        			matrix[i][j] = 0

        for j in range(c):
        	if mc[j] == 0:
        		for i in range(r):
        			matrix[i][j] = 0


