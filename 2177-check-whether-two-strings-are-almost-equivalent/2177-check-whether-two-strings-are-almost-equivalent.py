from collections import Counter
class Solution:
    def checkAlmostEquivalent(self, word1: str, word2: str) -> bool:
        mp1 = Counter(word1)
        mp2 = Counter(word2)
        for key,val in mp1.items():
            if key in mp2:
                if  abs(mp1[key]-mp2[key]) > 3:
                    return False
            else:
                if mp1[key] > 3:
                    return False
        for key,val in mp2.items():
            if key in mp1:
                if abs(mp1[key]-mp2[key]) > 3:
                    return False
            else:
                if mp2[key] > 3:
                    return False
        return True