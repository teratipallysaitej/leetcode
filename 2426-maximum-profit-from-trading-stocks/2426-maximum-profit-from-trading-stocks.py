class Solution:
    def maximumProfit(self, present: List[int], future: List[int], budget: int) -> int:    
        profit = [future[i] - present[i] for i in range(len(present))]
        n = len(present)
        
        # Initialize the DP table
        dp = [[0] * (budget + 1) for _ in range(n + 1)]

        for i in range(1, n + 1):
            for w in range(budget + 1):
                if present[i-1] <= w:  # Check if the item can be bought with the current budget
                    # Choose the maximum of including the item or not
                    dp[i][w] = max(profit[i-1] + dp[i-1][w-present[i-1]], dp[i-1][w])
                else:
                    # If the item cannot be bought, take the previous result
                    dp[i][w] = dp[i-1][w]
                    
        return max(0, dp[n][budget])  # The result will be in the last cell of the DP table