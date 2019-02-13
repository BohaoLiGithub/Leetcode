#DP
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
        for i in range(2,length - 1):
            dp[i] = max(dp[i-2] + nums[i], dp[i-1])
        dp[-1] = dp[-2]
       
        
        dp1 = [0 for _ in range(length)]
        dp1[0], dp1[1] = nums[1], max(nums[1],nums[2])
        for i in range(2,length-1):
            dp1[i] = max(dp1[i-2] + nums[i+1], dp1[i-1])
        return max(dp1[-2],dp[-2])