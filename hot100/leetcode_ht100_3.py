class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        right = 0
        l = []
        res = 0
        while right < len(s):
            if s[right] not in l:
                l.append(s[right])
                right += 1
            
            else:
                l.append(s[right])
                while l.count(s[right]) > 1:
                    l.pop(0)
                right += 1
            
            res = max(res, len(l))
        
        return res
    

sol = Solution()
s = "pwwkew"
print(sol.lengthOfLongestSubstring(s))