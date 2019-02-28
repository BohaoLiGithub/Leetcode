# https://www.youtube.com/watch?v=DJ4a7cmjZY0
# We need to consider each coin to see how this coin changes the total amount of ways that we can change
# For each coin, there are only two possibilities : add this coin or not add this coin

class Solution(object):
    def change(self, amount, coins):
        """
        :type amount: int
        :type coins: List[int]
        :rtype: int
        """
        dp = [0] * (amount+1)
        dp[0] = 1
        for coin in coins:
            for i in range(int(coin),amount+1):
                dp[i] += dp[i-int(coin)]
        return dp[-1]