class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        memo = {}

        # dp(s,i,p,j): s[:i]和p[:j]能否匹配
        def dp(s, i, p, j):
            m = len(s)
            n = len(p)
            # base case
            # pattern完成匹配
            if j == n:
                return i == m
            # s走完了
            if i == m:
                # p*肯定成对存在
                if (n - j) % 2 == 1:
                    return False
                
                while j + 1 < n:
                    # 判断是否为p*
                    if p[j + 1] != '*':
                        return False
                    j += 2
                return True

            # 设立备忘录，减少重复计算
            key = str(i) + ',' + str(j)
            if key in memo:
                return memo[key]
            
            # 一一匹配
            if s[i] == p[j] or p[j] == '.':
                if j + 1 < n and p[j + 1] == '*':
                    # dp(s, i, p, j + 2):*匹配多个
                    # dp(s, i + 1, p, j):*匹配零个
                    res = dp(s, i, p, j + 2) or dp(s, i + 1, p, j)
                else:
                    # 接着匹配
                    res = dp(s, i + 1, p, j + 1)
            
            else:
                # *匹配零个
                if j + 1 < n and p[j + 1] == '*':
                    res = dp(s, i, p, j + 2)
                else:
                # 匹配失败
                    res = False
            
            memo[key] = res
            return res

        return dp(s, 0, p, 0)            

