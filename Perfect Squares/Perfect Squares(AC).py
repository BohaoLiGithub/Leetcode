class Solution(object):
    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 0:
            return 0
        dp = list(0 for _ in range(n+1))
        for j in range(1,n+1):
            dp[j] = 2**32 -1
        for j in range(1,n+1):
            perfectList = [m**2 for m in range(1,int(j**0.5)+1)]
            #print (perfectList)
            for perfectNum in perfectList:
                    sub = dp[j - perfectNum]
                    if not sub == 2**32 - 1:
                        dp[j] = min(dp[j], sub + 1)
        #print (dp)
        return dp[-1]