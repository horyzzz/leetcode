from collections import Counter

class Solution:
    def singleNumber(self, nums) -> int:
        dd = Counter(nums)
        for x, y in dd.items():
            if y == 1:
                return x
                      