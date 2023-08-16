class Solution(object):
    def maxSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        res = []
        arr = []
        for i in range(len(nums)):
            heapq.heappush(arr,[-1*nums[i],i])
            if i>=k-1:
                while True:
                    if arr:
                        z = heapq.heappop(arr)
                        if i-k+1 <= z[1] <= i:
                            res.append(-1*z[0])
                            heapq.heappush(arr,z)
                            break
                    else:
                        break
                
        return res