class Solution:
    def exchange(self, nums: List[int]) -> List[int]:
        n = len(nums)
        p2 = n - 1
        p1 = 0
        while p1 < p2:
            if nums[p1] % 2 == 0 and nums[p2] % 2 == 1:
                nums[p1], nums[p2] = nums[p2], nums[p1]
                p1 += 1
                p2 -= 1
            elif nums[p1] % 2 == 0:
                p2 -= 1
            elif nums[p2] % 2 == 1:
                p1 += 1
            
            else:
                p1 += 1
                p2 -= 1
        
        return nums