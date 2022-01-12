class Solution:
    def translateNum(self, num: int) -> int:
        num1 = str(num)
        n = len(num1)
        dp = [1 for _ in range(n)]
        dp[0] = 1
        for i in range(1, n):
            if int(num1[i-1] + num1[i]) >= 10 and int(num1[i-1] + num1[i]) <= 25:
                dp[i] = dp[i-1] + dp[i-2]
            else:
                dp[i] = dp[i-1]
        
        return dp[n-1]

s = 12258
sol = Solution()
print(sol.translateNum(s))