class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return
        dp = [nums[i] for i in range(len(nums))]
        dp[0] = nums[0]
        for idx in range(1,len(nums)):
            pre = dp[idx-1]
            if pre >= 0:
                dp[idx] = pre + nums[idx]
            else:
                dp[idx] = nums[idx]
        return max(dp)
                