class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rset = defaultdict(set)
        cset = defaultdict(set)
        sset = defaultdict(set)

        rows = len(board)
        cols = len(board[0])

        for r in range(rows):
            for c in range(cols):
                if board[r][c] == ".":
                    continue
                val = board[r][c]
                sq = (r//3, c//3)
                if val in rset[r] or val in cset[c] or val in sset[sq]:
                    return False
                rset[r].add(val)
                cset[c].add(val)
                sset[sq].add(val)

        return True
        