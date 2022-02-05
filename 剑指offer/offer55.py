class Solution:
    def canJump(self, nums) -> bool:
        n = len(nums)
        farthest = 0
        for i in range(n-1):
            farthest = max(farthest, i+nums[i])
            if farthest <= i:
                return False
                
        return farthest >= n - 1
        
nums = [3,2,1,0,4]
sol = Solution()
print(sol.canJump(nums))