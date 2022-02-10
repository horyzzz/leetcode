"""
    122. 买卖股票的最佳时机 II

    给定一个数组 prices ,其中 prices[i] 是一支给定股票第 i 天的价格。

    设计一个算法来计算你所能获取的最大利润。你可以尽可能地完成更多的交易（多次买卖一支股票）。

    注意:你不能同时参与多笔交易（你必须在再次购买前出售掉之前的股票）。

"""

class Solution:
    def maxProfit(self, prices) -> int:
        """
            动态规划
            空间:[i][j] (i in {0:'不持有', 1:'持有'} j:截至第j天的最大利润)
            可做动作:买,卖,不动

            初始状态:
            dp[0][0] = 0
            dp[1][0] = -prices[0]

            转移方程:
            dp[0][j] = max(dp[0][j-1], dp[1][j-1] + prices[j])
            dp[1][j] = max(dp[1][j-1], dp[0][j-1] - prices[j])

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
            dp[0][j] = max(dp[0][j-1], dp[1][j-1] + prices[j])
            dp[1][j] = max(dp[1][j-1], dp[0][j-1] - prices[j])
        
        return dp[0][n-1]      