class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        INF = 2147483647
        m,n = len(grid), len(grid[0])

        def bfs(i,j):
            seen = set()

            dirs = [(1,0), (-1,0), (0,1), (0,-1)]

            q = deque()
            q.append([i,j, 0])
            while q:
                cr, cc, steps = q.popleft()
                grid[cr][cc] = min(grid[cr][cc], steps)

                for dr, dc in dirs:
                    nr, nc = cr + dr, cc + dc
                    if nr < 0 or nr >= m or nc < 0 or nc >= n or (nr,nc) in seen:
                        continue
                    if grid[nr][nc] > 0:
                        seen.add((nr,nc))
                        q.append([nr,nc, steps + 1])

        for r in range(m):
            for c in range(n):
                if grid[r][c] == 0:
                    bfs(r,c)

        
        