class Solution:
    """
        剑指 Offer 10- II. 青蛙跳台阶问题
        一只青蛙一次可以跳上1级台阶，也可以跳上2级台阶。求该青蛙跳上一个 n 级的台阶总共有多少种跳法。

        状态转移方程: dp[i] = dp[i-1] + dp[i+2]
    """
    
    def numWays(self, n: int) -> int:
        if n <= 1:
            return 1
        dp = [0 for _ in range(n+1)]

        dp[0] = 1
        dp[1] = 1

        for i in range(2, n+1):
            dp[i] = dp[i-1] + dp[i-2]
        
        return dp[n] % 1000000007