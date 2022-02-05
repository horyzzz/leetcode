class Solution:
    """
        hory笨笨做法--遍历o(N)
    """
    def missingNumber_hory(self, nums) -> int:
        if nums == [0]:
            return 1
        for i in range(len(nums)):
            if nums[i] != i:
                return i
        return len(nums)
    

    """
        leetcode二分法 o(logN)
    """
    def missingNumber(self, nums) -> int:
        i, j = 0, len(nums) - 1
        while i <= j:
            m = (i + j) // 2
            if nums[m] == m: i = m + 1
            else: j = m - 1
        return i
