"""
    剑指 Offer 63. 股票的最大利润
"""
class Solution:
    def maxProfit(self, prices) -> int:
        """
            动态规划
            空间:[i][j] (i in {0:'不持有', 1:'持有'} j:截至第j天的最大利润)
            可做动作:买，卖，不动

            初始状态:
            dp[0][0] = 0
            dp[1][0] = -prices[0]

            转移方程:
            dp[0][j] = max(dp[0][j-1], dp[1][j-1] + prices[j])
            dp[1][j] = max(dp[1][j-1], -prices[j])

            最终状态:
            dp[0][n-1]
            
        """
        if not prices:
            return 0
        n = len(prices)
        dp = [[float("-inf") for _ in range(len(prices))] for _ in range(2)]
        dp[0][0] = 0
        dp[1][0] = -prices[0]
        for j in range(1, n):
            dp[0][j] = max(dp[0][j-1], dp[1][j-1]+prices[j])
            dp[1][j] = max(dp[1][j-1], -prices[j])
        
        return dp[0][n-1]