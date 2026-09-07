class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        """
        c
        bc

        bcc
        cbc
        need to consider each char as a start/part of alr existing?

        blank case = 0

        b
        c
        0
        
        ad
        zd
        d= d, + -1 on both side

        bc
        c
        1
        b
        cb
        1
        bcc
        cb
        1
        bcc
        cbc
        i

        ca
        crab
        c
        cra -1
        ca
        cra
        c
        cr -1
        c
        c
        cb -1 
        c

            ' c r a b t
        '   0 0 0 0 0 0
        c   0 1 1 1 1 1
        a   0 1 1 2 2 2 
        t   0 1 1 2 2 3
        """
        m = len(text1)
        n = len(text2)
        dp = [[0 for _ in range(n+ 1)] for _ in range(m + 1)]

        for t1 in range(m):
            for t2 in range(n):
                prev = dp[t1][t2]
                if text1[t1] == text2[t2]:
                    prev += 1
                dp[t1 + 1][t2 +1] = max(prev, dp[t1 + 1][t2], dp[t1][t2 +1])
        
        return dp[m][n]

                




        