class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        words = sorted(words, key = len)
        dp = [1]*len(words)
        i = len(words) - 1
        mx = 1
        n = len(words)
        for i in range(n-2,-1,-1):
            q = len(words[i])
            a = words[i]
            for j in range(i+1,n):
                b = words[j]
                if len(b) - q == 1:
                    for e in range(len(words[j])):
                        t = b[0:e]+b[e+1:]
                        if a == t:
                            dp[i] = max(dp[i],dp[j]+1)
                            mx = max(mx,dp[i])
        
        return mx