# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        head = ListNode(0)
        temp = head
        carry = 0
        while(l1 or l2):
            s = carry
            if l1:
                s += l1.val
                l1 = l1.next
            if l2:
                s += l2.val
                l2 = l2.next
            temp.next = ListNode(s%10)
            temp = temp.next
            carry = s//10
        if carry==1:
            node = ListNode(1)
            temp.next = node
        return head.next

            
