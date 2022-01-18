class Solution:
    def findMinDifference(self, timePoints) -> int:

        def getMinutes(t: str) -> int:
            return ((ord(t[0]) - ord('0')) * 10 + ord(t[1]) - ord('0')) * 60 + (ord(t[3]) - ord('0')) * 10 + ord(t[4]) - ord('0')

        n = len(timePoints)
        if n > 1440:
            return 0

        timePoints.sort()
        res = float('inf')
        t0 = getMinutes(timePoints[0])
        premin = t0
        for i in range(1, n):
            minutes = getMinutes(timePoints[i])
            res = min(minutes - premin, res)
            premin = minutes
        
        return min(res, t0 + 1440 - premin)

sol = Solution()
timepoints = ["23:59","00:00"]
print(sol.findMinDifference(timepoints))