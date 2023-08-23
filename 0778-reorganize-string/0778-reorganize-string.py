from collections import Counter
class Solution:
    def reorganizeString(self, s: str) -> str:
      res = Counter(s)
      sorted_counter = sorted(res.items(), key=lambda x: -x[1])
      indices_even = []
      indices_odd = []
      arr = [-1]*len(s)
      for i in range(len(s)):
        if i%2 == 0:
          indices_even.append(i)
        else:
          indices_odd.append(i)
      indices = indices_even + indices_odd
      for a,b in sorted_counter:
        while b > 0:
          i = indices.pop(0)
          arr[i] = a
          if i-1>=0:
            if arr[i-1] == a:
              print(arr)
              return ""
          if i+1 < len(s):
            if arr[i+1] == a:
              print(arr)
              return ""
          b -= 1
      return "".join(arr)