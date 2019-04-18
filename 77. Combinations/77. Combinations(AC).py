class Solution(object):
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        
        num_list = [i for i in range(1,n+1)]
        tmp = []
        self.res = []
        self.dfs(tmp,num_list,0,k)
        return self.res
    def dfs(self,tmp_list,num_list,index,k_re):
        if k_re == 0:
            res_ = list(tmp_list)
            self.res.append(res_)
            return
        for idx in range(index,len(num_list)):
            tmp_list.append(num_list[idx])
            self.dfs(tmp_list,num_list,idx+1,k_re-1)
            tmp_list.pop()