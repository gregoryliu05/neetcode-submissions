class Solution:
    def countSubstrings(self, s: str) -> int:
        cnt = 0
        """
        abba
        or aba
        """
        n = len(s)
        for i in range(n):
            # single
            l, r = i, i
            while l >= 0 and r < n and s[l] == s[r]:
                cnt += 1
                l -= 1
                r += 1
            # double
            l, r = i-1, i
            while l >= 0 and r < n and s[l] == s[r]:
                cnt += 1
                l -= 1
                r += 1

        return cnt
        