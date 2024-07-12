# using Recurssion: Time limit Exceed
class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        n = len(coins)
        return self.changeRecurssion(amount,coins,n)

    def changeRecurssion(self, amount: int, coins: List[int], n: int) -> int:

        if amount == 0:
            return 1                
        if n == 0:
            return 0
        if coins[n-1] <= amount:
            return self.changeRecurssion(amount-coins[n-1],coins,n) + self.changeRecurssion(amount,coins,n-1)
        else:
            return self.changeRecurssion(amount,coins,n-1)

#using dp: Time complexity: O(N*N) Space complexity: O(N*N)
class Solution:
    def change(self, amount: int, coins: List[int]) -> int:           
        n = len(coins)
        dp = [[0 for x in range(amount+1)] for x in range(n+1)]
        for i in range(n+1):
            dp[i][0] = 1
        for i in range(1,n+1):
            for j in range(1,amount+1):
                if coins[i-1] <= amount:
                    dp[i][j] = dp[i][j-coins[i-1]] + dp[i-1][j]
                else:
                    dp[i][j]= dp[i-1][j]
        return dp[n][amount]
                
        
