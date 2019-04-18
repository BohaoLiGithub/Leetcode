class Solution(object):
    def canPartitionKSubsets(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        if sum(nums) % k != 0:
            return False
        nums.sort()
        print(nums)
        self.sum_ =sum(nums) / k
        print(self.sum_)
        visited = [False for _ in range(len(nums))] 
        res = self.dfs(k,nums,0,0,visited,0)
        return res
                    
    def dfs(self,k,nums,current_sum,index,visited,count):
        if k == 1:
            return True
        if current_sum == self.sum_ and count > 0:
            return self.dfs(k-1,nums,0,0,visited,0)
        for idx in range(index,len(nums)):
            if not visited[idx] and current_sum + nums[idx] <= self.sum_:
                visited[idx] = True
                res = self.dfs(k,nums,current_sum + nums[idx],idx+1,visited,count+1)
                if res:
                    return True
                visited[idx] = False
        return False