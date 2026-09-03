class Solution:
    def solve(self, board: List[List[str]]) -> None:
        # edges
        # do a bfs or dfs if we see an O
        # if none of those O reach an edge we replace all those with x's
        rows = len(board)
        cols = len(board[0])
        rowEdges = set([0, rows-1])
        colEdges = set([0, cols-1])
        dirs = [(0,1), (0,-1), (1,0), (-1,0)]
        def bfs(r,c):
            print("start", (r,c))
            seen = set([(r,c)])

            queue = deque()
            queue.append((r,c))
            while queue:
                cr, cc = queue.popleft()
                seen.add((cr,cc))
                if cr in rowEdges or cc in colEdges:
                    return set()
                for dr, dc in dirs:
                    nr,nc = cr + dr, cc + dc 
                    if nr >= 0 and nr < rows and nc >= 0 and nc < cols:
                        notused = (nr,nc) not in seen
                        isO = board[nr][nc] == "O"
                        if (nr,nc) not in seen and board[nr][nc] == "O":
                            queue.append((nr,nc))
                            seen.add((nr,nc))

            return seen

        for r in range(rows):
            for c in range(cols):
                if board[r][c] == "O":
                    indices = bfs(r,c)
                    if len(indices) > 0:
                        for x,y in indices:
                            board[x][y] = "X"
                    

        