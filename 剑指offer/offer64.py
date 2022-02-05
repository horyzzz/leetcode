class Solution:
    def __init__(self) -> None:
        self.res = 0

    def sumNums(self, n: int) -> int:
        n > 1 and self.sumNums(n - 1)
        self.res += n
        return self.res

sol = Solution()
print(sol.sumNums(5))