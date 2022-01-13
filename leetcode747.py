import numpy as np

class Solution:
    def dominantIndex1(self, nums) -> int:
        """
            遍历
        """
        n = len(nums)
        if n <= 1:
            return -1
        maxx = max(nums)
        m_index = np.argmax(nums)

        i = 0
        while i < n:                
            if maxx < 2*nums[i] and i != m_index:
                return -1
            i += 1
        
        return m_index
    
    def dominantIndex(self, nums) -> int:
        """
            leetcode 【宫水三叶】简单模拟题
            找到最大值和次大值
        """
        n = len(nums)
        if n == 1:
            return 0
        a, b = -1, 0
        for i in range(1, n):
            if nums[i] > nums[b]:
                a, b = b, i
            elif a == -1 or nums[i] > nums[a]:
                a = i
        return b if nums[b] >= nums[a] * 2 else -1

sol = Solution()
print(sol.dominantIndex([0,0,3,2]))
        