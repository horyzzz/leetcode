class Solution:
    """
        除大小王外,所有牌无重复 ；
        设此 5 张牌中最大的牌为 max ,最小的牌为 min （大小王除外）,则需满足：
        max - min < 5

        作者：jyd
        链接：https://leetcode-cn.com/problems/bu-ke-pai-zhong-de-shun-zi-lcof/solution/mian-shi-ti-61-bu-ke-pai-zhong-de-shun-zi-ji-he-se/
        来源：力扣（LeetCode）
    """
    def isStraight(self, nums) -> bool:
        visited = []
        mi, ma = 14, 0
        for num in nums:
            if num == 0:
                continue
            if num in visited:
                return False
            else:
                visited.append(num)
            mi = min(mi, num)
            ma = max(ma, num)
        
        return ((ma - mi) < 5)

sol = Solution()
print(sol.isStraight([1,2,3,4,5]))