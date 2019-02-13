class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        length = len(nums)
        
        if length == 0:
            return 0
        elif length == 1:
            return nums[0]
        elif length == 2:
            return max(nums[0],nums[1])
        
        dp = [0 for _ in range(length)]
        dp[0] = nums[0]
        dp[1] = max(nums[0],nums[1])
        for i in range(2,length):
            dp[i] = max(dp[i-1],dp[i-2] + nums[i])
        return dp[-1]