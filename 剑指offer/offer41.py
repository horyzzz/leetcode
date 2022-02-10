from heapq import *

class MedianFinder1:

    """
        超时
    """

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.nums = []


    def addNum(self, num: int) -> None:
        if not self.nums:
            self.nums.append(num)
        else:
            i = 0
            while i < len(self.nums) and self.nums[i] < num:
                i += 1
            self.nums = self.nums[:i] + [num] + self.nums[i:]


    def findMedian(self) -> float:
        n = len(self.nums)
        if n > 0 and n % 2 == 0:
            i1 = n // 2
            i2 = n // 2 + 1
            return (self.nums[i1-1] + self.nums[i2 - 1])/2
        elif n % 2 == 1:
            return self.nums[n//2]
        
class MedianFinder:

    """
    作者: jyd
    链接: https://leetcode-cn.com/problems/shu-ju-liu-zhong-de-zhong-wei-shu-lcof/solution/mian-shi-ti-41-shu-ju-liu-zhong-de-zhong-wei-shu-y/
    """
    def __init__(self):
        self.A = [] # 小顶堆,保存较大的一半
        self.B = [] # 大顶堆,保存较小的一半

    def addNum(self, num: int) -> None:
        if len(self.A) != len(self.B):
            heappush(self.A, num)
            heappush(self.B, -heappop(self.A))
        else:
            heappush(self.B, -num)
            heappush(self.A, -heappop(self.B))

    def findMedian(self) -> float:
        return self.A[0] if len(self.A) != len(self.B) else (self.A[0] - self.B[0]) / 2.0


# Your MedianFinder object will be instantiated and called as such:
obj = MedianFinder()
obj.addNum(1)
obj.addNum(2)
param_1 = obj.findMedian()
print(param_1)
obj.addNum(3)
param_2 = obj.findMedian()
print(param_2)
