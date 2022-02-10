"""
    123. 买卖股票的最佳时机 III

    给定一个数组,它的第 i 个元素是一支给定的股票在第 i 天的价格。

    设计一个算法来计算你所能获取的最大利润。你最多可以完成 两笔 交易

"""
class Solution:
    def maxProfit(self, prices) -> int:
        """
            动态规划
            空间:[i][j][k] (i in {0:'不持有', 1:'持有'} j:第几次交易 k:截止第k天)
            可做动作:买,卖,不动

            初始状态:
            dp[0][0][:] = 0
            dp[1][0][0] = -prices[0]

            转移方程:
            dp[0][j][k] = max(dp[1][j-1][k-1] + prices[k], dp[0][j][k-1])
            dp[1][j][k] = max(dp[1][j][k-1], dp[0][j-1][k-1] - prices[k])

            最终状态:
            max(dp[0][0][n-1], dp[0][1][n-1], dp[0][2][n-1], dp[0][3][n-1], dp[0][4][n-1])       
        """        
        
        if not prices:
            return 0
        n = len(prices)
        dp = [[[float("-inf") for _ in range(n)] for _ in range(5)] for _ in range(2)]
        dp[0][0][:] = [0 for _ in range(n)]
        dp[1][1][0] = -prices[0]
        
        for j in range(1, 5):
            for k in range(1, n):
                dp[0][j][k] = max(dp[1][j-1][k-1] + prices[k], dp[0][j][k-1])
                dp[1][j][k] = max(dp[1][j][k-1], dp[0][j-1][k-1] - prices[k])
        
        return max(dp[0][0][n-1], dp[0][1][n-1], dp[0][2][n-1], dp[0][3][n-1], dp[0][4][n-1])

sol = Solution()
prices = [1,2,3,4,5]
print(sol.maxProfit(prices))