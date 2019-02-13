class Solution(object):
    def summaryRanges(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        res = []
        start = 0
        while not start == len(nums):
            end = self.helper(start,nums)
            if not start == end:    
                str1 = str(nums[start])+"->"+str(nums[end])
                res.append(str1)
            else:
                res.append(str(nums[start]))
            start = end+1
        return res  
                
    def helper(self,start,nums):
        val = nums[start]
        if start == len(nums) - 1:
            return start
        for i in range(start+1,len(nums)):
            if nums[i] - val == 1:
                print ('in for if')
                val = nums[i]
                if i == len(nums)-1:
                    return i
            else:
                return i - 1