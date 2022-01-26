class Solution:
    def findContinuousSequence(self, target: int):
        i = 0
        j = 0
        l = list(range(1, target+1))
        res = []
        while i <= j < (target+1)//2:
            if sum(l[i: j + 1]) < target:
                j += 1
            elif sum(l[i: j+1]) == target:
                res.append(l[i: j + 1])
                i += 1
                j = i
            else:
                i += 1
                j = i
        return res

sol = Solution()
print(sol.findContinuousSequence(15))

        