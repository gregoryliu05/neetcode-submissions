class Solution:
    """
    canot contain leading zero

    2026
    single digit only 1 way to decode if not 0

    10 -> 1, 10
    12 -> 1, 1,2, 12
    single digit + 1 if not 0
    if whole str is valid up to that also +1 right, no?

    1012
    1 = 1
    10 = 1 -> (10)
    101 = 1 -> (10, 1) if prev is 0 that also fucks it up
    1011 = (10, 1, 2), (10, 12)
    if prev can be combined with curr, that is + 1 
    1,1,2,3
    11,2,3
    11,23
    1,12,3
    1,1,23
    1,1,2
    11,2
    1,12

    1 = 1
    11 = (1,1), (11)
            FROM 11        FROM 1
    112 = (1,1,2), (11,2), (1,12)
    1127 = 1,1,2,7, (11,2,7), (1,12,7)

    1123 = (1,1,2,3) (11,2,3), (1,12,3) (11,23), (1,1, 23)

    dp[i] = dp[i-1] +dp[i-2]
    1120 = (1,1,20)

    """
    def numDecodings(self, s: str) -> int:
        valid = set([str(i) for i in range(1,27)])
        n = len(s)
        dp = [-1 for _ in range(n + 1)]
        dp[0] = 1
        dp[1] = 1 if s[0] != "0" else 0
        for i in range(1,n):
            dpi = i + 1
            char = s[i]
            if char == "0":
                if s[i-1] == "0" or (s[i-1] != "1" and s[i-1] != "2"):
                    return 0
                if s[i-1] == "2" and 6 < int(s[i]) <= 9:
                    return 0
                dp[dpi] = dp[dpi-2]
            else:
                nxt = dp[dpi-1]
                if s[i-1] == "1" or (s[i-1] == "2" and int(s[i]) <= 6):
                    nxt += dp[dpi-2]
                dp[dpi] = nxt
        print(dp)
        return dp[n]
        