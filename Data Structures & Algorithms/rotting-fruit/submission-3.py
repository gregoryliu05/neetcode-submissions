class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])

        cnt = 0
        rotten = deque()
        mins = 0
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    cnt += 1
                if grid[r][c] == 2:
                    rotten.append((r,c))
        dirs = [(1,0), (-1,0), (0,1), (0,-1)]
        if cnt == 0:
            return 0
        while rotten:
            for i in range(len(rotten)):
                r,c = rotten.popleft()
                for dr, dc in dirs:
                    nr, nc = r+ dr, c+ dc
                    if nr < 0 or nr >= rows or nc < 0 or nc >= cols:
                        continue
                    if grid[nr][nc] == 1:
                        rotten.append((nr,nc))
                        grid[nr][nc] = 2
                        cnt -= 1
            mins +=1 
            if cnt <=0:
                return mins

        

        return -1







        