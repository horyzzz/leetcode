from typing import List


class Solution:
    def trap(self, height: List[int]) -> int:
        res = 0
        if len(height) == 0:
            return 0
        n = len(height)
        lmax = [0 for _ in range(n)]
        rmax = [0 for _ in range(n)]
        lmax[0] = height[0]
        rmax[-1] = height[n-1]
        for i in range(1, n):
            lmax[i] = max(height[i], lmax[i - 1])
        for i in range(n - 2, -1, -1):
            rmax[i] = max(height[i], rmax[i + 1])
        
        for i in range(n):
            res += min(lmax[i], rmax[i]) - height[i]
            
        return res
    
sol = Solution()
l = [0,1,0,2,1,0,1,3,2,1,2,1]
print(sol.trap(l))