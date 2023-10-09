class Solution:
    def minOperations(self, s1, s2, x):
        diffs = [i for i in range(len(s1)) if s1[i] != s2[i]]

        if len(diffs) % 2 == 1:
            return -1
        if len(diffs) == 0:
            return 0
        
        dp_i_plus_two = 0
        dp_i_plus_one = x / 2

        for idx in reversed(range(len(diffs) - 1)):
            dp_i = min(
                    dp_i_plus_one + x / 2,
                    dp_i_plus_two + diffs[idx + 1] - diffs[idx]
                )
            dp_i_plus_two = dp_i_plus_one
            dp_i_plus_one = dp_i
        
        return int(dp_i)