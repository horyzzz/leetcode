class Solution:
    def exist(self, board, word: str) -> bool:
        n1 = len(board)
        n2 = len(board[0])
        visited = [[0 for _ in range(n2)] for _ in range(n1)]
        def dfs(i, j, k, visited):
            if not 0 <= i < n1 or not 0 <= j < n2 or board[i][j] != word[k] or visited[i][j]:
                return False
            visited[i][j] = 1
            if k == len(word) - 1:
                return True
            res = dfs(i, j+1, k+1, visited) or dfs(i, j-1, k+1, visited) or dfs(i+1, j, k+1, visited) or dfs(i-1, j, k+1, visited)
            visited[i][j] = 0
            return res
        for i in range(n1):
            for j in range(n2):
                if dfs(i, j, 0, visited):
                    return True
        return False