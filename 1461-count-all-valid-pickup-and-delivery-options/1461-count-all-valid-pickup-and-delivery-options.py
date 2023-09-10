
class Solution:
    def countOrders(self, n: int) -> int:
        if n ==1:
            return 1
        if n == 2:
            return 6
        c = 6
        e = 10**9+7
        for i in range(3,n+1):
            pos = (i-1)*2 + 1
            c = c*((pos)*(pos+1))//2

        return c%e