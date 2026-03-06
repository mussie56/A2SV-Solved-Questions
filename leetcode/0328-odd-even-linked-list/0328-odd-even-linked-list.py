# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        curr = head
        # if head.next:
        even = curr.next
        temp = even
        
        flag = False
        while even and even.next:
            curr.next = even.next
            curr = curr.next
            even.next = curr.next
            even = even.next

        curr.next = temp
            
        return head