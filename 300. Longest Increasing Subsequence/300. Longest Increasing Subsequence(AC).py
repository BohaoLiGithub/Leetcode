# DP 
#link： https://www.youtube.com/watch?v=fV-TF4OvZpk

class Solution(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        dp = [1 for _ in xrange(len(nums))]
        for j in xrange(1,len(nums)):
            for i in xrange(j):
                if nums[j] > nums[i]:
                    temp = dp[i] + 1
                    dp[j] = max(dp[j],temp)
        return max(dp)