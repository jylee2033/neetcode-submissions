# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # [2,4,6,8]
        # left head
        # right head

        fast_ptr = head.next
        slow_ptr = head

        while fast_ptr and fast_ptr.next:
            fast_ptr = fast_ptr.next.next
            slow_ptr = slow_ptr.next

        # slow_ptr is pointing at the middle
        # Reverse right side of Linked List
        # [None <- 6 <- 8 -> None]
        #         prev cur
        prev = None
        cur = slow_ptr.next
        slow_ptr.next = None

        while cur:
            nxt = cur.next # Store next node
            cur.next = prev # Switch direction 
            prev = cur
            cur = nxt

        cur = prev

        # Combine left half and right half
        right_cur = cur
        left_cur = head

        # [2,4,6,8]
        # [2,8,4,6]
        while right_cur:
            left_nxt = left_cur.next # Store 4
            right_nxt = right_cur.next # Store 6
            left_cur.next = right_cur # 2 points to 8
            right_cur.next = left_nxt # 8 points to 4
            left_cur = left_nxt # left_cur points to 4
            right_cur = right_nxt # right_cur points to 6