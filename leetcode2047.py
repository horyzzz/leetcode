import re

class Solution:
    def countValidWords0(self, sentence: str) -> int:
        s_l = sentence.split(' ')
        res = 0
        ss = []
        for s in s_l:
            if s.strip() and (re.fullmatch(r'[a-z]+\-{1}[a-z]+[\,\.\!]{0,1}', s) or re.fullmatch(r'[a-z]*[\,\.\!]{0,1}', s)):
                res += 1
                ss.append(s)
            else:
                continue
        
        return res, ss

    def countValidWords(self, sentence: str) -> int:
        def valid(s: str) -> bool:
            hasHyphens = False
            for i, ch in enumerate(s):
                if ch.isdigit() or ch in "!.," and i < len(s) - 1:
                    return False
                if ch == '-':
                    if hasHyphens or i == 0 or i == len(s) - 1 or not s[i - 1].islower() or not s[i + 1].islower():
                        return False
                    hasHyphens = True
            return True

        return sum(valid(s) for s in sentence.split())

sentence = "cat and  dog"
sol = Solution()
print(sol.countValidWords(sentence))