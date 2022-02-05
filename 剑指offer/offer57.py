class Solution:
    def twoSum(self, nums, target: int):
        n = len(nums)
        p1 = 0 
        p2 = n - 1
        while p1 < p2:
            if nums[p1] + nums[p2] < target:
                p1 += 1
            elif nums[p1] + nums[p2] > target:
                p2 -= 1
            else:
                return [nums[p1], nums[p2]]
        
        return []