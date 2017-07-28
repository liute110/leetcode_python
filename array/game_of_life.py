class Solution(object):
    def gameOfLife(self, board):
        """
        :type board: List[List[int]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        if not board: return
        for i in range(len(board)):
        	for j in range(len(board[0])):
        		count = self.find_live(board,i,j)
        		if count==3 and board[i][j]==0:
        			board[i][j] = 3
        		elif board[i][j]==1 and (count<2 or count>3):
        			board[i][j] = 2
        for i in range(len(board)):
        	for j in range(len(board[0])):
        		board[i][j] %= 2
    def find_live(self,board,i,j):
    	count = 0
    	for x in range(i-1,i+2):
    		for y in range(j-1,j+2):
    			if x<0 or y<0 or (x==i and y==j) or x>=len(board) or y>=len(board[0]):
    				continue 
    			elif board[x][y]==2 or board[x][y]==1:
    				count += 1
    	return count
