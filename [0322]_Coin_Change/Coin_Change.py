class Solution(object):

    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        dp = [amount + 1 for i in range(amount + 1)]
        dp[0] = 0
        n = len(coins)
        coins.sort()
        for i in range(1, amount + 1):
            for j in range(n):
                if coins[j] > i:
                    break
                dp[i] = min(dp[i], dp[i - coins[j]] + 1)
        if dp[amount] == amount + 1:
            return -1
        return dp[amount]
