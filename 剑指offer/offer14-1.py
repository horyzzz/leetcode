class Solution:
    def cuttingRope(self, n: int) -> int:
        """
            dp[n]长度为n的绳子划成m份的最大乘积
            # dp[i]:每次遍历j找出i的最大值,j*(i-j)剪绳子,j*dp[i-j]:不剪绳子
            dp[i] = max(dp[i], j * (i-j),  j * dp[i - j])
        """
        dp = [1 for _ in range(n+1)]
        dp[2] = 1
        for i in range(3, n+1):
            for j in range(2, i):
                # dp[i]:每次遍历j找出i的最大值,j*(i-j)剪绳子,j*dp[i-j]:不剪绳子
                dp[i] = max(dp[i], j * (i-j),  j * dp[i - j])

        return dp[n]