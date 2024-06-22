
class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        total = 0
        count = 0
        odd_count = 0
        odd_indices = [-1]

        # Record indices of odd numbers
        for i, num in enumerate(nums):
            if num % 2 == 1:
                odd_indices.append(i)
        
        odd_indices.append(len(nums))  # Append a sentinel value
        
        # Calculate the number of subarrays with exactly k odd numbers
        for i in range(1, len(odd_indices) - k):
            left = odd_indices[i] - odd_indices[i - 1]
            right = odd_indices[i + k] - odd_indices[i + k - 1]
            total += left * right
        
        return total
