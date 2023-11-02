class Solution:
    def maxPalindromes(self, s: str, k: int) -> int:
        res = 0
        lastp = -1

        def helper(l, r):
            nonlocal lastp, res
            while l >= 0 and r < len(s) and s[l] == s[r] and l > lastp:
                if r-l+1 >= k:
                    res += 1
                    lastp = r
                    break # find the shortest palindrome
                else:
                    l -= 1
                    r += 1
        
        for i in range(len(s)):
            helper(i, i)  # odd length
            helper(i, i+1)  # even length
        return res          