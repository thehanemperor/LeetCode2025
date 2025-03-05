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
        length = 1
        # root = old tail after loop
        while root.next:
            length += 1
            root = root.next
        oldtail = root
        oldtail.next = head

        k %= length
        root = head
        for i in range(length-k-1):
            root = root.next
        newhead = root.next
        root.next = None
        return newhead
        