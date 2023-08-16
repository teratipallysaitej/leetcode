from collections import deque

class Solution(object):
    def maxSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        if k == 1:
            return nums

        mq = deque()
        res = []

        for i in range(len(nums)):
            # Remove elements outside the current window
            while mq and mq[0] < i - k + 1:
                mq.popleft()

            # Remove elements that are less than the current element
            while mq and nums[mq[-1]] < nums[i]:
                mq.pop()

            # Add the current index to the queue
            mq.append(i)

            # If the current index is in the window, append the maximum element to the result
            if i >= k - 1:
                res.append(nums[mq[0]])

        return res
