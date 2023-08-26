class Solution:
    def findLongestChain(self, pairs: List[List[int]]) -> int:
        pairs.sort(key = lambda x:(x[0],x[1]))
        mn = 1
        dp = [1]*len(pairs)
        n = len(pairs)
        for i in range(n-2,-1,-1):
            for j in range(i+1,n):
                if pairs[i][1] < pairs[j][0]:
                    dp[i] = max(dp[i],dp[j]+1)
                    mn = max(mn,dp[i])
        return mn

