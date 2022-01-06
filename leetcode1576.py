import random
class Solution:
    def modifyString(self, s: str) -> str:
        if not s:
            return None
        alpha = ['a', 'b', 'c', 'd', 'e', 'f', 'g',
                'h', 'i', 'j', 'k', 'l', 'm', 'n',
                'o', 'p', 'q', 'r', 's', 't', 'u',
                'v', 'w', 'x', 'y', 'z']
        p1 = 0
        while p1 <= len(s) - 1:
            pre = s[p1 - 1] if p1 > 0 else ''
            aft = s[p1 + 1] if p1 < len(s) - 1 else ''
            if p1 < len(s) - 1:
                sub_end = s[p1+1:]
            else:
                sub_end = ''
            
            if s[p1] == '?':
                alpha1 = [x for x in alpha if x != pre and x != aft]
                random_alpha = random.randrange(0, len(alpha1))
                s = s[:p1] + alpha1[random_alpha] + sub_end
            
            p1 += 1
        return s

Sol = Solution()
s = "?z??s?"
re = Sol.modifyString(s)
print(re)
                

