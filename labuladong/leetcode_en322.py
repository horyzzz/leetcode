import numpy as np
class Solution:
    def coinChange1(self, coins, amount: int) -> int:
        # 设定memo记录
        memo = [-666 for _ in range(amount+1)]
        
        # dp(coins, amount):使用coins凑到amount的最小数量
        
        def dp(coins, amount):
            if amount == 0:
                return 0
            if amount < 0:
                return -1
            
            if memo[amount] != -666:
                return memo[amount]
            
            # 状态转移： dp(coins, amount) = min(res, dp(coins, amount-coin))
            res = np.float('inf')
            for coin in coins:
                subproblem = dp(coins, amount - coin)
                if subproblem == -1:
                    continue
                res = min(res, subproblem + 1)
            
            memo[amount] = -1 if res==np.float('inf') else res
            
            return memo[amount]
        return dp(coins, amount)
    

    def coinChange(self, coins, amount):
        # dp[amount] 凑到amount所需的最小硬币数
        dp = [amount + 1 for _ in range(amount+1)]
        dp[0] = 0

        for i in range(1, amount):
            for coin in coins:
                if i - coin < 0:
                    continue
                dp[i] = min(dp[i], dp[i-coin] + 1)
        
        res = -1 if dp[amount] == amount+1 else dp[amount]
        return res

