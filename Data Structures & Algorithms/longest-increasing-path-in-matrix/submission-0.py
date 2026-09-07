class Solution:
    """
    I don't need to keep track of longest path a int is part of; only the longest path that starts from it right?
    """
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        dirs = [(0,1), (0,-1), (1,0), (-1,0)]
        res = 0
        rows = len(matrix)
        cols = len(matrix[0])
        dp = [[-1 for _ in range(cols)] for _ in range(rows)]

        def dfs(cr, cc):
            if dp[cr][cc] != -1:
                return dp[cr][cc]
            longestPath = 1

            for dr, dc in dirs:
                nr, nc = cr + dr, cc+  dc
                if nr >= 0 and nr < rows and nc >= 0 and nc < cols:
                    if matrix[cr][cc] < matrix[nr][nc]:
                        longestPath = max(longestPath, 1 + dfs(nr,nc))
        
            dp[cr][cc] = longestPath
            return dp[cr][cc]

        
        for r in range(rows):
            for c in range(cols):
                if dp[r][c] == -1:
                    dfs(r,c)
                
                res = max(dp[r][c], res)

        return res
        