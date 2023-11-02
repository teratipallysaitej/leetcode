class Solution:
    def breakPalindrome(self, p: str) -> str:
        res = list(p)
        n = len(p)
        if n ==1 : return ""
        print(res)
        for i in range(n//2):
            if res[i] != 'a':
                res[i] = 'a'
                return ''.join(res)
        
        res[-1] = 'b'
        return ''.join(res)

