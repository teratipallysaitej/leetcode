class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        UF = {}
        n = len(points)
        for i in range(n):
            UF.setdefault(i, i)
        def find(x):
            if x != UF[x]:
                UF[x] = find(UF[x])
            return UF[x]
        def union(x, y):
            UF[find(x)] = find(y)

        q = []
        for i in range(n):
            for j in range(i+1,n):
                heapq.heappush(q,[abs(points[j][0]-points[i][0])+abs(points[j][1]-points[i][1]),[i,j]])
        c = 0
        d = 0
        while c < n-1:
            dis, [x, y] = heapq.heappop(q)
            a = find(x)
            b = find(y)
            if a != b:
                d += dis
                union(x,y)
                c += 1
        return d