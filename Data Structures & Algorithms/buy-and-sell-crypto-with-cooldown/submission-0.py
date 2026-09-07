class Solution:
    """
    len of 1 is 0
    1,2,3
    buy day1, sell day 3
    2,1,3
    do nothing day 1, buy day 2, sell day 3
    2,1,3,5
    do nothing day 1, buy day 2, do nothing day 3, sell day 4
    choices: skip, or buy/sell

    """
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        if n == 1:
            return 0
        dp = dict()

        def dfs(i, canBuy):
            if i >= n:
                return 0
            if (i, canBuy) in dp:
                return dp[(i, canBuy)]
            
            if canBuy:
                # buy
                buy = dfs(i+1, not canBuy) - prices[i]
                

                # skip
                skip = dfs(i+1, canBuy)
                dp[(i, canBuy)] = max(buy, skip)
            else:
                # sell
                sell = dfs(i + 2, not canBuy) + prices[i]

                # skip
                skip = dfs(i + 1, canBuy)

                dp[(i, canBuy)]= max(sell,skip)

            return dp[(i, canBuy)]
        
        dfs(0, True)
        return dp[(0, True)]
        


                