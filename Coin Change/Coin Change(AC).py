class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        if amount <= 0:
            return 0
        if len(coins) == 0:
            return -1
        coins.sort(reverse = True)
        #print (coins)
        dp = list(0 for _ in range(amount+1))
        
        for i in range(1,amount+1):
            dp[i] = 2**32-1
        for j in range(1,amount+1):
            for coin in coins:
                if coin <= j:
                    sub = dp[j-coin]
                    if not sub == 2**32-1:
                        dp[j] = min(dp[j],sub+1)
        
        return dp[-1] if not dp[-1] == 2**32-1 else -1