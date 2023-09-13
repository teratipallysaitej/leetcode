class Solution:
    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:
        arr = []
        for x,i in enumerate(groupSizes):
            arr.append((i,x))
        arr.sort(key = lambda x:x[0])
        res = []
        val = arr[0][0]
        temp = [arr[0][1]]
        val -= 1
        for i in range(1,len(arr)):
            if val == 0:
                res.append(temp)
                temp = []
                val = arr[i][0]
            temp.append(arr[i][1])
            val -= 1
        res.append(temp)
        return res
