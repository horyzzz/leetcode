class Solution:
    """
        剑指 Offer 10- I. 斐波那契数列
    """
    def fib(self, n: int) -> int:
        if n == 0:
            return 0
        if n == 1:
            return 1

        dp = [0 for _ in range(n+1)]
        dp[0] = 0
        dp[1] = 1

        for i in range(2, n + 1):
            dp[i] = dp[i - 1] + dp[i - 2]
        
        return dp[n] % 1000000007

    def fib1(self, n: int) -> int:
        MOD = 10 ** 9 + 7
        if n < 2:
            return n
        p, q, r = 0, 0, 1
        for i in range(2, n + 1):
            p = q
            q = r
            r = (p + q) % MOD
        return r


sol = Solution()
n = [0, 1, 5]
print([sol.fib(x) for x in n])

        


            