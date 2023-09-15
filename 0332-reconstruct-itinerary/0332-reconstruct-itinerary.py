from collections import defaultdict
class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        d = defaultdict(list)
        # for a,d1 in tickets:
        #     hel.add(a)
        #     hel.add(d1)
        #     d[a] = []
        #     d[d1] = []
        for a, d1 in tickets:
            d[a].append(d1)
        for a in d:
            d[a].sort()
        # count = len(hel)
        def helper(node, it):
            global res
            # z = count
            # for key in d:
            #     if len(d[key]) == 0:
            #         z -= 1

            if len(it) == len(tickets) + 1:
                return True
            if node not in d:
                return False
            # if z == 0:
            #     q = it[:]
            #     res.append(q)
            for i,n in enumerate(d[node]):
                it.append(n)
                d[node].pop(i)
                # print(it, n, d)
                if helper(n,it): return True
                it.pop(-1)
                d[node].insert(i,n)

            return False
        it = []
        it.append("JFK")
        helper("JFK", it)
        # for key in d:
        #     if len(d[key]):
        #         res.append(key)
        #         helper(key)
        return it

