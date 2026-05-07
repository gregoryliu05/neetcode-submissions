class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = [1 for _ in range(n)]
        fromEnd = [0 for _ in range(n)]
        pre = 1
        for i in range(1,n):
                # fromEnd[n-1-i] = nums[n-1-i]
            pre *= nums[i-1]
            res[i] = pre
            # fromEnd[n-1-i] = nums[n-1-i] * fromEnd[n-i]
        # 1,2,8,48
        # 48, 48, 24, 6
        # 48, 
        post = 1
        for i in range(n-2, -1, -1):
            post *= nums[i+1]
            res[i] *= post
        return res        