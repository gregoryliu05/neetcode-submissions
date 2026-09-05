class Solution:
    def rob(self, nums: List[int]) -> int:
        n= len(nums)
        dp = [-1 for _ in range(n)]
        dp[n-1]= nums[n-1]

        def dfs(i):
            if i >= len(nums):
                return 0
            if dp[i] != -1:
                return dp[i]
            # choose or skip
            cur = nums[i]
            choose = cur + dfs(i +2)
            skip = dfs(i+1)

            dp[i] = max(choose,skip)
            return dp[i]
        dfs(0)
        return dp[0]

        
        