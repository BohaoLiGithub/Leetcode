class Solution(object):
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        n = len(s)
        dp = [0] * n
        if s[0] == '0':
            return 0
        dp[0] = 1
        if n == 1 :
            return dp[0]
        
        if s[1] == '0':
            if s[0] == '1' or s[0] == '2':
                dp[1] = 1
            else:
                return 0
        else:
            if s[0] == '1' or (s[0] == '2' and 0 < int(s[1]) <= 6):
                dp[1] = 2
            else:
                dp[1] = 1
        
        for i in range(2,n):
            prev = int(s[i-1])
            cur = int(s[i])
            if cur == 0:
                if prev == 1 or prev == 2:
                    dp[i] = dp[i-2]
                else:
                    return 0
            else:
                if prev == 1 or (prev == 2 and cur <= 6):
                    dp[i] = dp[i-1] + dp[i-2]
                else:
                    dp[i] = dp[i-1]
        return dp[-1]
        
        