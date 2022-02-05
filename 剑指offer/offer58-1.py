class Solution:
    def reverseWords(self, s: str) -> str:
        sl = s.strip().split(' ')
        p1 = 0
        p2 = len(sl) - 1
        while p1 < p2:
            sl[p1], sl[p2] = sl[p2], sl[p1]
            p1 += 1
            p2 -= 1
        res = ' '.join([x for x in sl if len(x) > 0])
        return res

sol = Solution()
s = "a good   example"
print(sol.reverseWords(s))