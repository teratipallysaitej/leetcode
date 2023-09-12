class Solution:
    def minDeletions(self, s: str) -> int:
        d = {}
        mx = 0
        for i in s:
            if i not in d:
                d[i] = 1
                mx = max(mx,d[i])
            else:
                d[i] += 1
                mx = max(mx,d[i])
        arr = [0]*mx        
        free = []
        
        for i in d:
            arr[d[i]-1] += 1
        del1 = 0
        for i in range(len(arr)):
            if arr[i] == 0:
                free.append(i)
            if arr[i] > 1:
                q = arr[i] - 1
                while free and q>0:
                    a = free.pop(-1)
                    del1 += i - a
                    q -= 1
                if len(free) == 0 and q >= 1:
                    del1 += (i+1)*q
            
        return del1
        