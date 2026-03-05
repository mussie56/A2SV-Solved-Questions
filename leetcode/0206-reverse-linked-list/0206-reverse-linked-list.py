# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        prev = head
        curr = prev.next
        nxt = curr
        while curr:
            nxt = curr.next
            curr.next = prev
            if prev == head:
                prev.next = None
            prev = curr
            curr = nxt
        return prev