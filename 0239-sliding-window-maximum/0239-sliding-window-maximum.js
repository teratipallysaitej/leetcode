/**
 * @param {number[]} nums
 * @param {number} k
 * @return {number[]}
 */
var maxSlidingWindow = function(nums, k) {
     if (k === 1) {
            return nums;
        }

        let mq = [];
        let res = [];

        for (let i = 0; i < nums.length; i++) {
            // Remove elements outside the current window
            while (mq.length && mq[0] < i - k + 1) {
                mq.shift();
            }

            // Remove elements that are less than the current element
            while (mq.length && nums[mq[mq.length - 1]] < nums[i]) {
                mq.pop();
            }

            // Add the current index to the queue
            mq.push(i);

            // If the current index is in the window, append the maximum element to the result
            if (i >= k - 1) {
                res.push(nums[mq[0]]);
            }
        }

        return res;

};