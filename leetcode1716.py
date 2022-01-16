class Solution:
    def totalMoney(self, n: int) -> int:
        n7 = n // 7
        l7 = n % 7
        if n <= 7:
            return sum(range(1, n+1))
        first_week = sum(range(1, 8))
        res = 0
        for i in range(n7):
            res += (7 * i + first_week)

        for j in range(l7):
            res += (n7 + 1 + j) 
        
        return res

sol = Solution()
n = 20
print(sol.totalMoney(n))