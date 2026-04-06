# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # [] -> []
        # [0,1,2,3] -> [3,2,1,0]
        # None -> 0 -> 1
        # 1 -> 0 -> None

        prev = None
        
        while head is not None:
            nxt = head.next
            head.next = prev
            prev = head
            head = nxt

        return prev