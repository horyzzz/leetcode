from collections import deque

class Solution:
    def highestPeak(self, isWater):
        m, n = len(isWater), len(isWater[0])
        res = [[water - 1 for water in row] for row in isWater]

        # BFS
        # 从水域出发， 保存所有水域 ----使用deque提速
        q = deque()
        for i in range(m):
            for j in range(n):
                if isWater[i][j] == 1:
                    q.append((i, j))
        
        # BFS遍历
        while q:
            i, j = q.popleft()
            for x, y in [(i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)]:
                # 找到尚未遍历的陆地
                if 0 <= x < m and 0 <= y < n and res[x][y] == -1:
                    res[x][y] = res[i][j] + 1
                    q.append((x, y))
        
        return res

isWater = [[0,1],[0,0]]
sol = Solution()
print(sol.highestPeak(isWater=isWater))