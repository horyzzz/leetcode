from collections import Counter


class Solution:
    """
        方法1 很慢
    """
    def firstUniqChar1(self, s: str) -> str:
        if not s:
            return ' '
        tmp = []
        drop = []
        for x in s:
            if x in tmp or x in drop:
                if x in tmp:
                    tmp.remove(x)
                if x not in drop:
                    drop.append(x)
            else:
                tmp.append(x)
        res = tmp[0] if tmp else ' '
        return res

    """
        方法2
    """

    from collections import Counter
    def firstUniqChar(self, s: str) -> str:
        if not s:
            return ' '
        di = Counter(s)
        for x in di.keys():
            if di[x] == 1:
                return x
        return " "

        
sol = Solution()
s = 'leetcode'
print(sol.firstUniqChar(s))