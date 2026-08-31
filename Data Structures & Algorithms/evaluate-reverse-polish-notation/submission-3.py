class Solution:
    def evalRPN(self, tokens: List[str]) -> int: 
        stack = []
        ops = set(["+", "-", "*", "/"])
        for t in tokens:
            if t in ops:
                num2 = stack.pop()
                num1 = stack.pop()
                res = 0
                if t == "+":
                    res = num1 + num2
                elif t == "-":
                    res = num1 - num2
                elif t == "*":
                    res = num1 * num2
                else:
                    res = num1/num2
                stack.append(int(res))
            else:
                stack.append(int(t))

        return int(stack[-1])


        