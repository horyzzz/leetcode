import sys
from collections import deque
sys.setrecursionlimit(10^10)
max_d = 10^6
class Solution:
    """
        zhr dfs 迭代次数溢出
    """
    def isEscapePossible0(self, blocked, source, target) -> bool:
        visited = []
        def dfs(i, j):
            if [i, j] in blocked or [i, j] in visited or i < 0 or i >= max_d or j < 0 or j >= max_d:
                if visited:
                    visited.pop(-1)
                return False
            if [i, j] == target:
                return True
            
            visited.append([i, j])

            
            return dfs(i+1, j) or dfs(i-1, j) or dfs(i, j+1) or dfs(i, j-1)
        
        return dfs(source[0], source[1])

EDGE, MAX, BASE, DIR = int(1e6), int(1e5), 131, [(1, 0), (-1, 0), (0, 1), (0, -1)]

class Solution:
    """
        利用bfs（leetcode答案）
    """
    def isEscapePossible(self, blocked, source, target) -> bool:
        block = {p[0] * BASE + p[1] for p in blocked}
        n = len(blocked)
        MAX = n * (n-1)//2 # 可直接使用 1e5
        def check(a, b):
            vis = {a[0] * BASE + a[1]}
            d = deque([a])
            while len(d) and len(vis) <= MAX:
                x, y = d.popleft()
                if x == b[0] and y == b[1]:
                    return True
                for dx, dy in DIR:
                    nx, ny = x + dx, y + dy
                    if nx < 0 or nx >= EDGE or ny < 0 or ny >= EDGE:
                        continue
                    h = nx * BASE + ny
                    if h in block or h in vis:
                        continue
                    d.append((nx, ny))
                    vis.add(h)
            return len(vis) > MAX
        return check(source, target) and check(target, source)

sol = Solution()
blocked = []
source = [0,0]
target = [999999,999999]
print(sol.isEscapePossible(blocked, source, target))







            
            

        