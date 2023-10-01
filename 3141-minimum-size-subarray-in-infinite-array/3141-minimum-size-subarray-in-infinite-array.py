
class Solution:
    def minSizeSubarray(self, nums: List[int], target: int) -> int:
        d = target//sum(nums)+2
        k = nums*d
        print(k)
        n = len(k)
        mn = n
        st = 0
        s = k[0]
        f = False
        for i in range(1,n):
            s += k[i]
            while s > target:
                s -= k[st]
                st += 1
            if s == target:
                mn = min(mn, i -st + 1)
                f = True
        if not f:
            return -1
        return mn