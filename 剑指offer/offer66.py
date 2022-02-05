class Solution:
    def constructArr(self, a):
        b = [1 for _ in range(len(a))]

        # 维护从0~i-1的积
        for i in range(1, len(a)):
            b[i] = b[i - 1] * a[i -1]
        
        tmp = 1
        # 维护从i+1~n-1的积
        for j in range(len(a) - 2, -1, -1):
            tmp *= a[j + 1]
            b[j] *= tmp

        return b