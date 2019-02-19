class Solution(object):
    def canPartition(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        #nums.sort()
        sum_ = sum(nums)
        if sum_ % 2 == 1:
            return False
        target = sum_ / 2
        dp = [False for _ in xrange(target+1)]
        dp[0] = True
        for i in range(len(nums)):
            print('i: '+ str(nums[i]))
            for j in range(target,nums[i]-1,-1):
                print('j: '+ str(j))
                dp[j] = dp[j] or dp[j-nums[i]]
                print('dp'+str(dp[j]))
        #print(dp)
        return dp[-1]