class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        """
            动态规划
            设字符 s[i] 左边距离最近的相同字符为 s[j], 即 s[j] = s[i]
        """
        if not s:
            return 0
        dict = {}
        n = len(s)
        dp = [1 for _ in range(n)]
        dp[0] = 1
        dict[s[0]] = 0
        maxx = 1
        for i in range(1, n):
            j = dict.get(s[i], -1)
            dict[s[i]] = i
            
            if dp[i - 1] < i - j:
                # 当 dp[i-1] < i-j,说明字符 s[j] 在子字符串 dp[i-1]区间之外,则 dp[i] = dp[i-1] + 1
                dp[i] = dp[i-1] + 1
            else:
                # 当 dp[i-1] > i-j,说明字符 s[j] 在子字符串 dp[i-1]区间之内,dp[i]的左边界由s[j]决定
                dp[i] = i - j
            maxx = max(maxx, dp[i])

        return maxx

sol = Solution()
s = "abcabcbb"
print(sol.lengthOfLongestSubstring(s))