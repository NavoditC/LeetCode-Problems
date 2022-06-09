# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        temp1 = head
        temp2 = head
        i=0
        while temp2 and i<=n:
            temp2=temp2.next
            i+=1
        if temp2==None and i==n:
            return head.next
        while temp2:
            temp1=temp1.next
            temp2=temp2.next
        temp1.next = temp1.next.next
        return head

        
