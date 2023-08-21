class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        z = [0]*len(s)
        j = 0
        i = 1
        k = 0
        while i < len(s):
            if s[i] == s[j]:
                j += 1
                z[i] = j
                i += 1
            elif s[i] != s[j] and j > 0:
                j = z[j-1]
            else:
                z[i] = 0
                i += 1
      
        y = len(z)                
        return z[y-1] != 0 and y%(y-z[y-1]) == 0