# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def merge2Lists(self,l1: Optional[ListNode],l2: Optional[ListNode]) -> Optional[ListNode]:
        head = ListNode(0)
        h = head
        while (l1 and l2):
            if l1.val<l2.val:
                node= ListNode(l1.val)
                h.next = node
                h = h.next
                l1=l1.next
            else:
                node= ListNode(l2.val)
                h.next = node
                h = h.next
                l2=l2.next
        while(l1):
            node = ListNode(l1.val)
            h.next=node
            h = h.next
            l1=l1.next
        while(l2):
            node = ListNode(l2.val)
            h.next = node
            h = h.next
            l2 = l2.next
        return head.next
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        k = len(lists)
        if k==0:
            return None
        i,j = 0,len(lists)-1
        while(j>0):
            i = 0
            while(i<j):
                head = self.merge2Lists(lists[i],lists[j])
                lists[i]=head
                i+=1
                j-=1
        return lists[0]
