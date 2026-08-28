class Solution:
    """
    true -> s2 has a contiguous substring that has same chars as s1

    len(s2) >= len(s1)

    s1: a
    s2: aa

    s1: abc
    s2: bacc

    s1: abc
    s2: bbbcc

    s1: aba
    s2: abcdaacbaa
        01234567
    s1: aabbcc
    s2: sassaabcabc
    
    a:-1
    b:2
    c:2
    

    whats the most efficient way to check for permutation?
    is there like a check we can use to know when to check or not
    or have to check every time?
    how can we reuse prev work/eliminate redundant work?
    build dict of s1, if at any point its empty we return true
    do like a sliding window
    """
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1set = set(s1) # O(26)
        m,n = len(s1), len(s2)
        if n < m:
            return False
        s1dict = {}
        for s in s1:
            if s not in s1dict:
                s1dict[s] = 0
            s1dict[s] += 1

        for i in range(n):
            # add back
            if i >= m:
                add = s2[i-m]
                if add in s1set:
                    if add not in s1dict:
                        s1dict[add] = 0
                    s1dict[add] += 1
                    if s1dict[add] == 0:
                        del s1dict[add]

            # remove from end
            remove = s2[i]
            if remove in s1set:
                if remove not in s1dict:
                    s1dict[remove] = -1
                else:
                    s1dict[remove] -= 1
                    if s1dict[remove] == 0:
                        del s1dict[remove]
            
            # check for empty
            if not s1dict:
                return True


        return False

        