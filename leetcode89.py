"""
    根据镜像性
"""
class Solution:
    def grayCode(self, n: int) -> List[int]:
        dp = [[0, 1]]
        i = 1
        while i <= n:
            next_part = [x + 2 ** i for x in dp[i-1]]
            dp_i = dp[i-1] + next_part[::-1]
            dp.append(dp_i)
            i += 1
        return dp[n-1]