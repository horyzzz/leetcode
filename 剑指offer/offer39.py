from collections import Counter

class Solution:
    def majorityElement(self, nums) -> int:
        dict1 = Counter(nums)
        n = len(nums) / 2
        for i, j in dict1.items():
            if j >= n:
                return i
        
