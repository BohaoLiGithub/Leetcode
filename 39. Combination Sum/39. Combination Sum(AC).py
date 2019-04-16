class Solution(object):
    def __init__(self):
        self.res  = []
    
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        candidates.sort()
        temp_list = []
        result = []
        self.dfs(temp_list,candidates,0,target,result)
        return result
            
    def dfs(self,list_,candidates,index,target,result):
        if target == 0:
            res = list(list_)
            result.append(res)
            return
        for idx in range(index,len(candidates)):
            if candidates[idx] > target:
                break
            list_.append(candidates[idx])
            self.dfs(list_,candidates,idx,target - candidates[idx],result)
            list_.pop()