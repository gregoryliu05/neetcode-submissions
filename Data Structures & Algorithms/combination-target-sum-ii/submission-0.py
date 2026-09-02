class Solution:
    """
    1,2,2

    """
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        res = []

        def backtracking(i, cur, arr):
            if cur == target:
                res.append(arr.copy())
                return
            if i >= len(candidates):
                return
            if cur > target:
                return
            
            
            seen = set()
            for j in range(i, len(candidates)):
                if candidates[j] not in seen:
                    seen.add(candidates[j])
                    arr.append(candidates[j])
                    backtracking(j +1, cur + candidates[j], arr)
                    arr.pop()


            return

        # use or skip
        backtracking(0, 0, [])
        return res  
        