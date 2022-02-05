class Solution:
    def strToInt(self, str: str) -> int:
        str1 = str.strip()
        if not str1:
            return 0
        if str1[0] not in ['+', '-'] and not str1[0].isdigit():
            return 0
        res = 0
        i = 1
        if str1[0] == '+':
            stack = [1]
        elif str1[0] == '-':
            stack = [-1]
        else:
            stack = [1, int(str1[0])]
        
        n = len(str1)
        while i < n and str1[i].isdigit():
            stack.append(int(str1[i]))
            i += 1
        
        n1 = len(stack[1:])
        j = 0
        while j < n1:
            res += stack.pop() * (10 ** j)
            j += 1
            if res >= 2 ** 31 - 1 and stack[0] == 1:
                return 2 ** 31 - 1
            elif stack[0] == -1 and res >= 2 ** 31:
                return -2 ** 31
                
        res1 = stack[0] * res 
        return res1


sol = Solution()
print(sol.strToInt("   +0 123"))