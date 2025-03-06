# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        small = ListNode()
        large = ListNode()
        smallCurr = small
        largeCurr = large
        while head:
            if head.val < x:
                smallCurr.next = head
                smallCurr = smallCurr.next
            else:
                largeCurr.next = head
                largeCurr = largeCurr.next
            head = head.next
        largeCurr.next = None    
        smallCurr.next = large.next
        return small.next

            