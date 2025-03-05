# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode()
        dummy.next = head
        self.dfs(head,dummy,n)
        return dummy.next

    def dfs(self,head,prev,n):
        if not head:
            return 1
        num = self.dfs(head.next,head,n)
        
        if num == n:
            prev.next = head.next
            head.next = None

        return num + 1
        