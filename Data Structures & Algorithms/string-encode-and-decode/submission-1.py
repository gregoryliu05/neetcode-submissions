class Solution:
    # list of strings to single str
    # so that I can turn that str into a list of strs
    # what strs are needed to be encoded?
    # hi, hello, hey -> hihellohey or smth
    def encode(self, strs: List[str]) -> str:
        res = []
        for s in strs:
            ln = str(len(s))
            res.append(ln + "/" + s)

        print("".join(res))
        return "".join(res)


    def decode(self, s: str) -> List[str]:
        res = []
        i = 0
        ln = ""
        while i < len(s):
            if s[i] != "/":
                ln += s[i]
            else: 
                string = []
                for j in range(i + 1, i +1 + int(ln)):
                    string.append(s[j])
                res.append("".join(string))
                i = i + int(ln)
                ln = ""
            i += 1

        return res
