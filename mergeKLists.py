# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        heap = []
        
        for idx, num in enumerate(lists):
            while num:
                heappush(heap, num.val)
                num = num.next


        dummy = ListNode()
        curr = dummy

        while heap:
            node = ListNode(val=heappop(heap))
            curr.next = node
            curr = curr.next

        return dummy.next
