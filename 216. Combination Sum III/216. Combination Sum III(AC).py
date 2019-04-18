class Solution(object):
    def combinationSum3(self, k, n):
        """
        :type k: int
        :type n: int
        :rtype: List[List[int]]
        """
        self.result = list()
        tmp_list = []
        list_num = [i for i in range(1,10)]
        self.dfs(list_num,tmp_list,0,k,n)
        return self.result
        
    def dfs(self,list_num,tmp_list,index,k_remain,n_remain):
        if k_remain == 0 and n_remain == 0:
            res_ = list(tmp_list)
            self.result.append(res_)
            return
        
        for idx in range(index,len(list_num)):
            if list_num[idx] > n_remain:
                return
            tmp_list.append(list_num[idx])
            self.dfs(list_num,tmp_list,idx+1,k_remain-1,n_remain-list_num[idx])
            tmp_list.pop()
    