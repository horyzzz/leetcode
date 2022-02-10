"""
地上有一个m行n列的方格,从坐标 [0,0] 到坐标 [m-1,n-1] 。一个机器人从坐标 [0, 0] 的格子开始移动,
它每次可以向左、右、上、下移动一格（不能移动到方格外）,也不能进入行坐标和列坐标的数位之和大于k的格子。
例如,当k为18时,机器人能够进入方格 [35, 37] ,因为3+5+3+7=18。但它不能进入方格 [35, 38],因为3+5+3+8=19。
请问该机器人能够到达多少个格子？
"""
class Solution:
    def movingCount(self, m: int, n: int, k: int) -> int:
        """
            dfs
        """
        def getsum(num):
            k1 = num // 10
            k2 = num - num // 10 * 10
            return k1 + k2
        
        def dfs(i, j, visited):
            if not 0 <= i < m or not 0 <= j < n or visited[i][j] or getsum(i) + getsum(j) > k:
                return 0
            else:
                visited[i][j] = 1
                # 向右的格数加上向下的格数+1
                return dfs(i+1, j, visited) + dfs(i, j+1, visited) + 1
        
        visited = [[0 for _ in range(n)] for _ in range(m)]

        return dfs(0, 0, visited)
