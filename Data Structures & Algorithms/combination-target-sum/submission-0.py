class Solution:
    """
    2,5,6,9
    target = 9

    """
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        def backtracking(i, cur, arr):
            if i == len(nums):
                return
            if cur > target:
                return 
            if cur == target:
                res.append(arr.copy())
                return 
            for j in range(i, len(nums)):
                arr.append(nums[j])
                backtracking(j, cur + nums[j], arr)
                arr.pop()
            return
            
            
        backtracking(0, 0, [])

        return res
        