class Solution:
    """
        滑动窗口 好慢。。。。
    """
    def containsNearbyDuplicate1(self, nums, k: int) -> bool:
        n = len(nums)
        al = []
        for i in range(n):
            if i > k:
                al.pop(0)
            if nums[i] in al:
                return True
            al.append(nums[i])
        return False

    def containsNearbyDuplicate2(self, nums, k: int) -> bool:
        """
            使用set----快一点
        """
        s = set()
        for i, num in enumerate(nums):
            if i > k:
                s.remove(nums[i - k - 1])
            if num in s:
                return True
            s.add(num)
        return False


    def containsNearbyDuplicate(self, nums, k: int) -> bool:
        """
            哈希表----最快
        """
        pos = {}
        for i, num in enumerate(nums):
            if num in pos and i - pos[num] <= k:
                return True
            pos[num] = i
        return False

sol = Solution()
nums = [99, 99]
k = 2
print(sol.containsNearbyDuplicate(nums, k))