# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        # if not lists or not lists[0]:
        #     return None
        k = len(lists)
        merging = True
        dummy = ListNode()
        root = dummy
        index = 0
        while merging:
            end = 0
            nodeI = None
            minNum = 999999
            for i in range(k):
                # print(i, lists[i])
                if not lists[i]:
                    end += 1
                    continue
                if lists[i].val < minNum:
                    minNum = lists[i].val
                    nodeI = i
            
            
               
            if end == k:
                merging = False
            else:
                curr = ListNode(minNum)
                root.next = curr
                root = root.next
                lists[nodeI] = lists[nodeI].next
        
        return dummy.next