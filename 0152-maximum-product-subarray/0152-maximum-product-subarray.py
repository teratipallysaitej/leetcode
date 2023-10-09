class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        mx = nums[0]
        mn = nums[0]
        m1 = nums[0]
        
        for i in range(1,len(nums)):
            temp = max(mx*nums[i],mn*nums[i],nums[i])
            mn = min(mx*nums[i],mn*nums[i],nums[i])
            mx = temp
            m1 = max(mx,m1)
            
        return m1    