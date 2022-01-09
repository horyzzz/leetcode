class Solution:
    def slowestKey(self, releaseTimes, keysPressed: str) -> str:
        if len(releaseTimes) <= 1 or len(keysPressed) <= 1:
            return keysPressed[0]
        p1 = 0
        p2 = 1
        maxx = releaseTimes[0]
        max_alpha = keysPressed[0]
        while p2 < len(keysPressed):
            if releaseTimes[p2] - releaseTimes[p1] == maxx:
                if keysPressed[p2] > max_alpha:
                    max_alpha = keysPressed[p2]
                p1 += 1
                p2 += 1    
                continue
            if releaseTimes[p2] - releaseTimes[p1] > maxx:            
                maxx = releaseTimes[p2] - releaseTimes[p1]                    
                max_alpha = keysPressed[p2]
            p1 += 1
            p2 += 1
            
        return max_alpha


releaseTimes = [1,2]
keysPressed = "ba"      
sol = Solution()
print(sol.slowestKey(releaseTimes=releaseTimes, keysPressed=keysPressed))