
class Solution:
    def countOrders(self, n: int) -> int:
        if n ==1:
            return 1
        c = 1
        e = 10**9+7
        for i in range(2,n+1):
            c = c*(((i-1)*2 + 1)*((i-1)*2 + 1+1))//2

        return c%e