class Solution:
    def maxArea(self, heights: List[int]) -> int:
        res= 0
        n= len(heights)
        l= 0 
        r = n-1
        while l < r:
            cur = min(heights[l], heights[r]) * (r -l)
            res = max(cur,res)
            if heights[l]> heights[r]:
                r -=1
            else:
                l+=1



        return res
        