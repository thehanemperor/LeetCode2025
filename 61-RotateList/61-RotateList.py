# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or not head.next:
            return head

        root = head
        length = 0
        while root:
            length += 1
            root = root.next

        k %= length
        if k == 0:
            return head
        
        meet = length - k
        i = 0
        prev = None
        root = head
        while i < meet:
            i+=1
            prev = root
            root = root.next

        
        prev.next = None
        end = root
        while end and end.next:
            end = end.next
        
        end.next = head
        return root