class Solution:
    """
        dfs 
        字符串加减运算
    """
    def isAdditiveNumber(self, num: str) -> bool:
        if len(num) < 3:
            return False
        
        def str_add(a: str, b: str) -> str:
            """
                定义字符串加减运算
                从后往前加
            """
            i, j, res, one = len(a) - 1, len(b) - 1, [], 0
            while i >= 0 or j >= 0:
                curA = curB = 0
            
                if i >= 0:
                    curA = int(a[i])
                    i -= 1
                
                if j >= 0:
                    curB = int(b[j])
                    j -= 1
                
                cur = curA + curB + one

                if cur >= 10:
                    cur %= 10
                    one = 1
                else:
                    one = 0
                
                res.append(str(cur))
                
            if one:
                res.append('1')
            
            return ''.join(res[::-1])
        
        def dfs(first_start: int, second_start: int) -> bool:
            """
                dfs
                first_start: 第一个数字的起始ind
                second_start: 第二个数字的起始ind
            """
            last_start = 0      # 上一个数字的起始ind

            while second_start < len(num):
                # 首位为0,返回False
                if (num[last_start] == '0' and first_start > last_start + 1) or (num[first_start] == '0' and second_start > first_start + 1):
                    return False
                
                s = str_add(num[last_start:first_start], num[first_start:second_start])

                if num[second_start:second_start + len(s)] != s:
                    return False
                
                last_start = first_start
                first_start = second_start
                second_start = second_start + len(s)
            
            return True
        
        # 遍历第一个数字起始位,第二个数字起始位的所有可能
        for i in range(len(num) - 1):
            for j in range(i+1, len(num)):
                if dfs(i, j):
                    return True
        
        return False


sol = Solution()
num = '199001200' 
print(sol.isAdditiveNumber(num))