class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for s in strs:
            slen = len(s)
            res += str(slen) + "#" + s
        
        return res


    def decode(self, s: str) -> List[str]:
        i = 0
        res = []
        while i < len(s):
            # get str len
            slen = ""
            while s[i] != "#":
                slen += s[i]
                i += 1
            slen = int(slen)
            ss = ""
            for j in range(i +1, i + 1 + slen):
                ss += s[j]
            res.append(ss)
            i += slen + 1

        
        return res

                
