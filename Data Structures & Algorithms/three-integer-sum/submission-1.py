class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        sn = sorted(nums)
        res = []
        for i in range(len(sn)):
            l, r = i + 1, len(sn) - 1
            if i> 0 and i < len(sn) -1 and sn[i] == sn[i-1]:
                continue
            while l < r:
                if sn[i] + sn[l] + sn[r] == 0:
                    res.append([sn[i], sn[l], sn[r]])
                    l += 1
                    while l < r and sn[l] == sn[l-1]:
                        l += 1
                elif sn[i] + sn[l] + sn[r] > 0:
                    r -= 1
                else:
                    l += 1
        
        return res

        