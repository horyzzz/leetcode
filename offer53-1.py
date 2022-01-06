class Solution:
    def search(self, nums, target: int) -> int:
        p1 = 0
        p2 = -1
        while p1 < len(nums):
            if nums[p1] == target:
                if p2 == -1:
                    p2 = p1
                if p1 == len(nums) - 1 or nums[p1+1] != target:
                    return p1 - p2 + 1
            p1 += 1
        return 0

sol = Solution()
nums = [2, 2]
target = 2

print(sol.search(nums=nums, target=target))