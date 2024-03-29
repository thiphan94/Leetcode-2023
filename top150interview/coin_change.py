from typing import List


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # dp = [amount + 1] * (amount + 1)
        dp = [float("inf")] * (amount + 1)
        dp[0] = 0
        print(dp)
        for i in range(1, amount + 1):
            for j in coins:
                if i - j >= 0:
                    dp[i] = min(dp[i], 1 + dp[i - j])

        # return dp[amount] if dp[amount] != amount + 1 else -1
        return dp[amount] if dp[amount] != float("inf") else -1
