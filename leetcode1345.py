from collections import *

"""
https://leetcode-cn.com/problems/jump-game-iv/solution/gong-shui-san-xie-noxiang-xin-ke-xue-xi-q9tb1/

"""
class Solution:
    def minJumps(self, arr) -> int:
        n = len(arr)
        mp = defaultdict(list)
        for i, num in enumerate(arr):
            mp[num].append(i)
        dist = [float('inf')] * n
        d = deque([0])
        dist[0] = 0
        while len(d) > 0:
            t = d.popleft()
            step = dist[t]
            if t == n - 1:
                return step
            for ne in mp[arr[t]]:
                if dist[ne] == float('inf'):
                    d.append(ne)
                    dist[ne] = step + 1
            mp.pop(arr[t])
            if dist[t + 1] == float('inf'):
                d.append(t + 1)
                dist[t + 1] = step + 1
            if t and dist[t - 1] == float('inf'):
                d.append(t - 1)
                dist[t - 1] = step + 1
        return -1

sol = Solution()
arr = [100,-23,-23,404,100,23,23,23,3,404]
print(sol.minJumps(arr))
