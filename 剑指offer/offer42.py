class Solution:
    def maxSubArray(self, nums) -> int:
        """
            dp[i]: 截止到第i位的最大连续子数组和
            状态转移方程
            dp[i] = max(dp[i-1]+nums[i](向右并入), nums[i](重新开始))

        """
        n = len(nums)
        dp = [-101 for _ in range(n)]
        maxs = nums[0]
        dp[0] = nums[0]
        for i in range(1, n):
            dp[i] = max(nums[i], dp[i-1] + nums[i])
            maxs = max(maxs, dp[i])
        return maxs