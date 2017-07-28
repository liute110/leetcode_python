#coding=utf8
import sys
class Solution(object):
    def combinationSum3(self, k, n):
        """
        :type k: int
        :type n: int
        :rtype: List[List[int]] 
        """
        self.res = []
        self.ele = []
        self.sub_cs3(1,k,n)
        return self.res

    def sub_cs3(self,index,k,n):
        if n < 0: return 
        if n == 0 and len(self.ele) == k:
            self.res.append(self.ele[:])
            return 
        for i in range(index,10):      
            self.ele.append(i)
            self.sub_cs3(i+1,k,n-i)
            self.ele.pop(-1)



print Solution().combinationSum3(3,7)





