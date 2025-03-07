# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        newHead = None
        kTail = None
        root = head
        while root:
            count = 0
            root = head
            while count < k and root:
                count +=1
                root = root.next
            if count == k:
                groupHead = self.reverse(head,k)

                if not newHead:
                    newHead = groupHead
                if kTail:
                    kTail.next = groupHead

                kTail = head
                head = root


        if kTail:
            kTail.next = head
        
        return newHead if newHead else head


    def reverse(self,start,k):
        newHead = None
        root = start
        while k:
            after = root.next
            root.next = newHead
            newHead = root
            root = after
            k -= 1

        return newHead
        
    