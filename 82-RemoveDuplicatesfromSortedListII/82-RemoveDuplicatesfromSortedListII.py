# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        dummy.next = head
        prev = dummy
        root = head
        while root:
            found = False
            while root.next and root.next.val == root.val:
                found = True
                root = root.next
            if found:
                prev.next = root.next
                
            else:
                # prev.next = root
                prev = root
            
            root = root.next

        return dummy.next