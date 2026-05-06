class Solution:
    """
    can choose k = bananas eating rate
    we can eat k bananas from the pile, can only eat max of 1 pile in 1 hr
    the max k we can choose is essentially max(piles) 
    min possible k would be 1
    how do we know if a k is too fast?

    we need the min eating speed
    """
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)
        k = r
        # if the current k is valid, we check the lower one and update our min
        # if the current k isn't valid, we go higher
        def isValid(rt):
            total = 0
            for pile in piles:
                hrs = math.ceil(pile/ rt)
                total += hrs
                if total > h:
                    return False
            return True

        while l <= r:
            m = l + (r-l) //2
            if isValid(m):
                k = min(k, m)
                r = m - 1
            else:
                l = m+ 1

        return k
        