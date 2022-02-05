class Solution:
    def permutation(self, s: str):
        n = len(s)
        res = set()
        visited = [0 for _ in range(n)]
        path = []

        def dfs(i):
            if i == n:
                res.add(''.join(path))
                return 
            for j in range(n):
                if visited[j]:
                    continue
                visited[j] = 1
                path.append(s[j])
                dfs(i + 1)
                path.pop(-1)
                visited[j] = 0
        
        dfs(0)


        return list(res)
            
            
sol = Solution()
print(sol.permutation("abc"))
                    
                
                