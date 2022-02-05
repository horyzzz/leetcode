class Solution:
    def isNumber(self, s: str) -> bool:
        # remove blank
        def scanInteger():
            nonlocal s, i
            if i < len(s) and s[i] in {'+', '-'}:
                i += 1
            return scanUnsignedInteger()
        
        def scanUnsignedInteger():
            nonlocal s, i
            start = i
            while i < len(s) and s[i].isdigit():
                i += 1
            return i > start
        
        s = s.strip()
        if not s:
            return False
        
        i = 0
        isNumeric = scanInteger()
        if i < len(s) and s[i] == '.':
            i += 1
            isNumeric = scanUnsignedInteger() or isNumeric
        
        if i < len(s) and s[i] in ['e', 'E']:
            i += 1
            isNumeric = isNumeric and scanInteger()
        
        return isNumeric and i == len(s)
