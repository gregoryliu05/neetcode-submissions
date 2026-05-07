class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        fromStart = []
        fromEnd = [0 for _ in range(n)]
        for i in range(n):
            if i == 0:
                fromStart.append(nums[i])
                fromEnd[n-1-i] = nums[n-1-i]
            else:
                fromStart.append(nums[i] * fromStart[i-1])
                fromEnd[n-1-i] = nums[n-1-i] * fromEnd[n-i]
        # 1,2,8,48
        # 48, 48, 24, 6
        # 48, 
        print(fromStart, fromEnd)
        res = [1 for _ in range(n)]
        for i in range(n):
            if i > 0:
                res[i] *= fromStart[i-1]
            if i < n-1:
                res[i] *= fromEnd[i+1]

        return res        