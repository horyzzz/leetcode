class Solution:
    """
        dfs 递归 笨笨的
    """
    def findNumberIn2DArray1(self, matrix, target: int) -> bool:
        n = len(matrix)
        m = len(matrix[0])
        visited = [[0 for _ in range(m)] for _ in range(n)]
        def dfs(i, j, visited, target):
            if i < 0 or i >= n or j < 0 or j >= m or visited[i][j]:
                return
            if matrix[i][j] == target:
                return True
            if matrix[i][j] < target:
                visited[i][j] = 1
                return dfs(i + 1, j, visited, target) or dfs(i, j + 1, visited, target)
            elif matrix[i][j] > target:
                visited[i][j] = 1
                return dfs(i - 1, j, visited, target) or dfs(i, j - 1, visited, target)
        
        if dfs(0, 0, visited, target) :
            return True
        else:
            return False
        

    """
        线性查找
    """
    def findNumberIn2DArray(self, matrix, target: int) -> bool:
        if not matrix:
            return False
        n = len(matrix)
        m = len(matrix[0])
        i = 0
        j = m - 1
        while i < n and j >= 0:
            if matrix[i][j] == target:
                return True
            elif matrix[i][j] <  target:
                i += 1
            else:
                j -= 1
        return False
            
    

matrix = [[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]]
target = 23
sol = Solution()
print(sol.findNumberIn2DArray(matrix=matrix, target=target))