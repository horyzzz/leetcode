class Solution:
    def increasingTriplet(self, nums) -> bool:
        """
            贪心算法
            为了找到递增的三元子序列,first和second应该尽可能地小,此时找到递增的三元子序列的可能性更大。
        """
        if len(nums) < 3:
            return False
        n = len(nums)
        first = nums[0]
        second = float('inf')
        for i in range(n):
            num = nums[i]
            if num > second:
                # 找到递增三元组
                return True
            elif num > first:
                # 待定第二个元素---找到尽可能小的second
                second = num
            else:
                # 找到尽可能小的first
                first = num
        
        return False
            

sol = Solution()
s = [1,5,0,4,1,3]
print(sol.increasingTriplet(s))