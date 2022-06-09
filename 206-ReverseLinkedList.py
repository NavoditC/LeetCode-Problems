# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        past = None
        while(head):
            ahead = head.next
            head.next = past
            past = head
            head = ahead
        return past
        
