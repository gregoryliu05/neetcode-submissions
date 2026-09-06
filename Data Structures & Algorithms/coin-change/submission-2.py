class Solution:
    """

    amt = 25
    16, 5, 1
    16, 5, 1, 1, 1, 1
    5, 5, 5, 5, 5

    0 1 2 3 4 5
    0 1 2 3 4 1

    if coin < curamt:
        1 + # of coins for curamt - coin val


    """
    def coinChange(self, coins: List[int], amount: int) -> int:
        
        dp = [float("inf") for _ in range(amount + 1)]
        dp[0] = 0
        for amt in range(1, amount + 1):
            for c in coins:
                if amt - c >= 0:
                    dp[amt] = min(dp[amt], 1 + dp[amt-c])
                
            
        
        return dp[amount] if dp[amount] != float("inf") else -1
        