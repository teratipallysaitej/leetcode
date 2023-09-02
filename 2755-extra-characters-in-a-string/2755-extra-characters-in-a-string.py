class Solution:
    def minExtraChar(self, s: str, dictionary: List[str]) -> int:
        n = len(s)
        print(s)
        dp = [1]*(len(s)+2)
        dp[0] = 0
        for i in range(n+1):
            dp[i+1] = dp[i]+1
            for word in dictionary:
                if i < len(word):
                    continue
                if s[i-len(word):i] == word:
                    print(word)
                    dp[i+1] = min(dp[i-len(word)+1], dp[i+1])
        return dp[-1] - 1

        