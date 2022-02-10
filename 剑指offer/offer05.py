"""
    剑指 Offer 05. 替换空格
    请实现一个函数,把字符串 s 中的每个空格替换成"%20"。
"""
class Solution:
    def replaceSpace(self, s: str) -> str:
        if not s:
            return ""
                
        blank_ind = [i for i, x in enumerate(s) if x == ' ']
        for i, j in enumerate(blank_ind):
            s = s[:j+2*i] + "%20" + s[j+2*i+1:]
        return s