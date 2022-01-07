class Solution:
    def maxDepth(self, s: str) -> int:
        maxd = 0
        depth = 0
        for x in s:
            if x == '(':
                depth += 1
            elif x == ')':
                depth -= 1
            maxd = maxd if depth < maxd else depth

        return maxd

s = "1"
sol = Solution()
print(sol.maxDepth(s))
