from functools import lru_cache
class Solution:
    def minOperations(self, s1: str, s2: str, x: int) -> int:
        n = len(s1)
        inf = 10**20
        @lru_cache(maxsize=None)
        def helper(ind: int,flip: int,extra: int) -> int:
            if ind == n:
                if extra > 0 or flip:
                    return inf
                else:
                    return 0
            b1 = int(s1[ind])
            b2 = int(s2[ind])
            if flip:
                b1 = 1 - b1
            
            ans = inf
            if b1 == b2:
                ans = min(ans,helper(ind+1,False,extra))
                # return ans
            else:
                ans = min(ans, helper(ind+1,True,extra)+1)
                ans = min(ans, helper(ind+1,False,extra+1)+x)
                if extra > 0:
                    ans = min(ans, helper(ind+1,False,extra-1))
            return ans
        z = helper(0,False,0)
        if z == inf:
            return -1
        return z




        
        