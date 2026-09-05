class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return nums[0]
        dp = [-1 for _ in range(n-1)]
        dp2 = dp.copy()
        def dfs(i, arr, d):
            if i >= len(arr):
                return 0
            if d[i] != -1:
                return d[i]
            
            choose = arr[i] + dfs(i+2, arr, d)
            skip = dfs(i+1, arr, d)
            d[i] = max(choose, skip)
            return d[i]

        return max(dfs(0, nums[:n-1], dp), dfs(0, nums[1:n], dp2))