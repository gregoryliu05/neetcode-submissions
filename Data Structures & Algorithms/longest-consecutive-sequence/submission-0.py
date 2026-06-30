class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numset = set(nums)
        res = 0
        cur = 1
        for n in numset:
            if n-1 not in numset:
                cur = 1
                c = n
                while c + 1 in numset:
                    c += 1
                    cur += 1
                res = max(cur,res)

        return res 
        