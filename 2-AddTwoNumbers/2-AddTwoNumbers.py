# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carry = 0
        dummy = ListNode()
        root = dummy
        while l1 or l2:
            first = l1.val if l1 else 0
            second = l2.val if l2 else 0
            curr = first + second + carry
            if curr >9:
                curr = curr % 10
                carry = 1
            else:
                carry = 0

            root.next = ListNode(curr)
            root = root.next
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None

        if carry:
            root.next = ListNode(1)
        return dummy.next 


        