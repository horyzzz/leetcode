"""
https://leetcode-cn.com/problems/stone-game-ix/solution/shi-zi-you-xi-ix-by-leetcode-solution-kk5f/
"""
class Solution:
    def stoneGameIX(self, stones) -> bool:
        cnt0 = cnt1 = cnt2 = 0
        for val in stones:
            if val % 3 == 0:
                cnt0 += 1
            elif val % 3 == 1:
                cnt1 += 1
            elif val % 3 == 2:
                cnt2 += 1
        
        if cnt0 % 2 == 0:
            return cnt1 >= 1 and cnt2 >= 1
        return cnt1 - cnt2 > 2 or cnt2 - cnt1 > 2