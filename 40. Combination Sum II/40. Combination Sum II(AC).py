class Solution(object):
    def __init__(self):
        self.result = []
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        tmp_res = []
        candidates.sort()
        self.dfs(0,candidates,target,tmp_res)
        return self.result
        
    def dfs(self,index,candidates,target,tmp_res):
        if target == 0:
            res = list(tmp_res)
            if res not in self.result:
                self.result.append(res)
            return
        
        for idx in range(index,len(candidates)):
            if candidates[idx] > target:
                break
            tmp_res.append(candidates[idx])
            #print(tmp_res)
            self.dfs(idx+1,candidates,target - candidates[idx],tmp_res)
            tmp_res.pop()