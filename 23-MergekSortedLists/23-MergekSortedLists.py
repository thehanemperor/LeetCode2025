# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        dummy = ListNode()
        root = dummy
        heap = []

        for node in lists:
            if node:
                heapq.heappush(heap,(node.val,{node}))

        while heap:
            val,node = heapq.heappop(heap)
            root.next = ListNode(val)
            root = root.next
            node = node.pop()
            if node.next:
                heapq.heappush(heap,(node.next.val, {node.next}))
        
        return dummy.next