# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head

        fast,slow = head,head
        while fast.next and fast.next.next:
            fast = fast.next.next
            slow = slow.next

        right = self.sortList(slow.next)
        slow.next = None
        left = self.sortList(head)
        merged = ListNode()
        temp = merged

        while left and right:
            if left.val <= right.val:
                merged.next = left
                left = left.next
            else:
                merged.next = right
                right = right.next
            merged = merged.next

        if left:
            merged.next = left
        if right:
            merged.next = right

        return temp.next