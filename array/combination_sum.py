class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        res = []
        elem = []
        self.sub_combination(candidates,target,res,elem,0,0)
        return res
        
    def sub_combination(self,candidates,target,res,elem,index,sub_sum):
    	if sub_sum > target: return
    	if sub_sum == target: 
    		res.append(elem[:])
    		return
    	for i in range(index,len(candidates)):
    		elem.append(candidates[i])
    		self.sub_combination(candidates,target,res,elem,i,sub_sum+candidates[i])
    		elem.pop()
