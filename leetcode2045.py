from collections import *

class Solution:
    def secondMinimum(self, n: int, edges, time: int, change: int) -> int:

        # 构建无向图
        graph = [[] for _ in range(n + 1)]
        for e in edges:
            x, y = e[0], e[1]
            graph[x].append(y)
            graph[y].append(x)
        
        # dist[i][0] 表示从 1 到 i 的最短路长度，
        # dist[i][1] 表示从 1 到 i 的严格次短路长度        
        dist = [[float('inf')] * 2 for _ in range(n + 1)]
        dist[1][0] = 0
        q = deque([(1, 0)])
        # (node, distance)

        # BFS ---- 本质上是计算经过节点数目
        while dist[n][1] == float('inf'):
            p = q.popleft()
            for y in graph[p[0]]:
                d = p[1] + 1
                # 更新最短长度
                if d < dist[y][0]:
                    dist[y][0] = d
                    q.append((y, d))
                # 更新次短长度
                elif dist[y][0] < d < dist[y][1]:
                    dist[y][1] = d
                    q.append((y, d))
        
        ans = 0
        # 计算所费时间
        for _ in range(dist[n][1]):
            # 绿 -> 红 -> 绿：时间周期为 2*change
            if ans % (change * 2) >= change:
                # 加上等待时间
                ans += change * 2 - ans % (change * 2)
            # 加上走路时间
            ans += time

        return ans

