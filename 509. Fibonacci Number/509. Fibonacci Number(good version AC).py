# DP 
# more fast

class Solution(object):
    def fib(self, N):
        """
        :type N: int
        :rtype: int
        """
        if N == 1:
            return 1
        elif N == 0:
            return 0
        fib = [0] * (N+1)
        fib[1] = 1 
        for i in range(2,N+1):
            fib[i] = fib[i-1] + fib[i-2]
        return fib[N]