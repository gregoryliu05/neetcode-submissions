class Solution:
    """
    231
    if target < mid
    min value left side (left)
    left side: 
    target > left side right (max) then go right? 
    612345
    345612

    if right

    345612
    456123

    l < m r < m 

    """
    def search(self, nums: List[int], target: int) -> int:
        n = len(nums)
        l = 0
        r = n-1
        while l <= r:
            m = l + (r-l)// 2
            print(m)
            if nums[m] == target:
                return m
            # find which side is sorted first
            if nums[l] <= nums[m]:
                if nums[l] <= target <= nums[m]:
                    r = m -1
                else:
                    l = m +1
            else:
                if nums[m] <= target <= nums[r]:
                    l = m + 1
                else:
                    r = m-1 



        return -1
        