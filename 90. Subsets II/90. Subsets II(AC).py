class Solution(object):
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        length = len(nums)
        nums.sort()
        if length == 0:
            return []
        self.result = [[]]
        self.result.append(nums)
        for target in range(1,length):
            tmp_list = []
            self.helper(target,0,nums,tmp_list)
        return self.result

            
    def helper(self,target,index,nums,list_):
        if target == 0 and list_ not in self.result:
            res_list = list(list_)
            self.result.append(res_list)
        for idx in range(index,len(nums)):
            list_.append(nums[idx])
            self.helper(target-1,idx+1,nums,list_)
            list_.pop()