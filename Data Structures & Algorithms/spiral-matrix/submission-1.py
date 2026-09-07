class Solution:
    """
        a b c d
    a   1 2 3 4
    b   5 6 7 8
    c   9 0 1 2
    d   3 4 5 6
    
    1 2
    3 4

    1 2 3
    4 5 6
    7 8 9

    tl tr
    bl br

    stop condition if tl > br
    
    right r, c+1
    down  r+1, c
    left  r, c-1
    up    r-1, c

    whats condition to move to next? 
    """
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        res = []
        rows = len(matrix)
        cols = len(matrix[0])

        tl ,tr = (0,0), (0, cols- 1)
        bl, br = (rows-1, 0), (rows-1, cols-1)
        # right, down, left, up 
        r, c = 0,0
        while tl[0] < br[0] and tl[1] < br[1]:
            # right
            while (r,c) != tr:
                print(r,c)
                res.append(matrix[r][c])
                c += 1
            tr = (tr[0] +1, tr[1] - 1)
            while (r,c) != br:
                print(r,c)
                res.append(matrix[r][c])
                r += 1
            br = (br[0] - 1, br[1] - 1)
            while (r,c) != bl:
                print(r,c)
                res.append(matrix[r][c])
                c -= 1
            bl = (bl[0] -1 , bl[1] + 1)

            while (r,c) != tl:
                print(r,c)
                res.append(matrix[r][c])
                r -= 1
            print("end" , r,c)
            tl = (tl[0] + 1, tl[1] + 1)
            print(tl, tr)
            print(bl, br)
            r += 1
            c += 1
        print(tl, tr)
        print(bl, br)
        for rr in range(tl[0], br[0] + 1):
            for cc in range(tl[1], tr[1] +1):
                res.append(matrix[rr][cc])
            

        return res
        