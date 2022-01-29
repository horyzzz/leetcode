class Solution:
    def maxSlidingWindow(self, nums, k: int):
        if not nums:
            return []
        p1 = 0
        res = []
        while p1 <= len(nums) - k:
            res.append(max(nums[p1: p1 + k]))
            p1 += 1
        return res