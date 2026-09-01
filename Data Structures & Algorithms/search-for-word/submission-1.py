class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows =len(board)
        cols = len(board[0])

        dirs =[(-1,0),(1,0),(0,-1),(0,1)]
        def dfs(r,c, seen, i):
            if i == len(word):
                print(i)
                return True

            for dr, dc in dirs:
                nr,nc = r +dr, c + dc
                if nr>=0 and nr < rows and nc>= 0 and nc < cols:
                    if (nr, nc) not in seen and board[nr][nc] == word[i]:
                        seen.add((nr,nc))
                        if dfs(nr,nc, seen, i+1):
                            return True
                        seen.remove((nr,nc))

            return False




        for r in range(rows):
            for c in range(cols):
                chr = board[r][c]
                if chr == word[0]:
                    if dfs(r,c, set([(r,c)]), 1):
                        return True
        return False


        