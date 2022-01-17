class Solution:
    def countVowelPermutation1(self, n: int) -> int:
        """
            dp[i][0] 以a结尾，长度为i的字符序列数
            dp[i][1] 以e结尾，长度为i的字符序列数
            dp[i][2] 以i结尾，长度为i的字符序列数
            dp[i][3] 以o结尾，长度为i的字符序列数
            dp[i][4] 以u结尾，长度为i的字符序列数

            dp[i][0] = dp[i-1][1] + dp[i-1][2] + dp[i-1][4]
            dp[i][1] = dp[i-1][0] + dp[i-1][2]
            dp[i][2] = dp[i-1][1] + dp[i-1][3]
            dp[i][3] = dp[i-1][2]
            dp[i][4] = dp[i-1][2] + dp[i-1][3]

            长度为n的字符序列数: sum(dp[n][0:5])
        """ 
        mod_n = 10 ** 9 + 7
        dp = [[1, 1, 1, 1, 1] for _ in range(n)]
        for i in range(1, n):
            dp[i][0] = (dp[i-1][1] + dp[i-1][2] + dp[i-1][4]) % mod_n
            dp[i][1] = (dp[i-1][0] + dp[i-1][2]) % mod_n
            dp[i][2] = (dp[i-1][1] + dp[i-1][3]) % mod_n
            dp[i][3] = (dp[i-1][2]) % mod_n
            dp[i][4] = (dp[i-1][2] + dp[i-1][3]) % mod_n
        
        return sum(dp[n-1]) % mod_n

    def countVowelPermutation(self, n):
        dp = (1, 1, 1, 1, 1)
        for _ in range(n - 1):
            dp = ((dp[1] + dp[2] + dp[4]) % 1000000007, (dp[0] + dp[2]) % 1000000007, (dp[1] + dp[3]) % 1000000007, dp[2], (dp[2] + dp[3]) % 1000000007)
        return sum(dp) % 1000000007


sol = Solution()
n = 2
print(sol.countVowelPermutation(n))
print(sol.countVowelPermutation1(n))