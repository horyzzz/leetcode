class Solution:
    def findRepeatNumber(self, nums) -> int:
        if not nums:
            return None
        dic = {}
        for x in nums:
            if x not in dic:
                dic[x] = 0
            else:
                return x