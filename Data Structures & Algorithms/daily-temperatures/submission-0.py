class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # monotonic decreasing stack
        res = [0 for _ in range(len(temperatures))]
        stack = []
        for i, t in enumerate(temperatures):
            # (index, temp)
            while stack and t > stack[-1][1]:
                print((i,t), stack[-1])
                res[stack[-1][0]] = (i - stack[-1][0])
                stack.pop()
            stack.append((i,t))
            


        return res

        