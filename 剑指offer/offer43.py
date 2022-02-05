from collections import Counter


class Solution:
    def countDigitOne(self, n: int) -> int:
        def find(l, r):
            if l >= r:
                return 0
            m = (l + r) // 2
            one_times = Counter(str(m))['1']
            return find(l, m) + one_times + find(m+1, r)
        
        return find(1, n+1)

sol = Solution()
print(sol.countDigitOne(12))