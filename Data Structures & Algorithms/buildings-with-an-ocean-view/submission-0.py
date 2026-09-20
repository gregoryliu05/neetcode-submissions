class Solution:
    def findBuildings(self, heights: List[int]) -> List[int]:
        stack = []
        for i in range(len(heights)):
            # 5 5
            while stack and heights[stack[-1]] <= heights[i]:
                stack.pop()
            stack.append(i)

        return stack 
        
        