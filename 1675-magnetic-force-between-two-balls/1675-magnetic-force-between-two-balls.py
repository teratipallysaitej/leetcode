from typing import List
import bisect

class Solution:
    def maxDistance(self, position: List[int], m: int) -> int:
        position.sort()
        if m == 2:
            return position[-1] - position[0]
        n = len(position)
        
        def isPossible(diff):
            count = 1
            last_position = position[0]
            
            for i in range(1, n):
                if position[i] - last_position >= diff:
                    count += 1
                    last_position = position[i]
                    if count == m:
                        return True
            return False
        
        start = 1  
        end = position[-1] - position[0]
        
        while start <= end:
            mid = start + (end - start) // 2
            if isPossible(mid):
                start = mid + 1
            else:
                end = mid - 1
        
        return end
