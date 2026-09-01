class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        def backtracking(open, close, arr):
            if open == close == n:
                res.append("".join(arr))
                return 
            if open < n:
                arr.append("(")
                backtracking(open + 1, close, arr)
                arr.pop()
            if open > close:
                arr.append(")")
                backtracking(open, close + 1, arr)
                arr.pop()
            return 

        backtracking(0,0,[])
        return res
        