# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        pq=[]
        prev=dummy=ListNode()
        for i in range(len(lists)):
            temp=lists[i]
            prev.next=temp
            while temp and temp.next:
                heappush(pq, temp.val)
                temp=temp.next
            if temp:
                heappush(pq, temp.val)
                prev=temp
        temp=dummy.next
        while temp:
            temp.val=heappop(pq)
            temp=temp.next
        return dummy.next    