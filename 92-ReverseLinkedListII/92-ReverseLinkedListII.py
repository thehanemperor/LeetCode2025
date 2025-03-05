# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if not head:
            return head

        prev = None
        curr = head
        while left>1:
            prev = curr
            curr = curr.next
            left -= 1
            right -= 1

        # the new tail
        tail = curr

        # boundry 
        con = prev

        while right >0:
            after = curr.next
            curr.next = prev
            prev = curr
            curr = after
            right -= 1

        tail.next = curr

        if con:
            con.next = prev
        else:
            head = prev

        return head

        
        

        