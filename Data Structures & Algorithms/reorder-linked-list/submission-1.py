# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head and not head.next:
            return
        fast,slow=head,head
        while fast.next and fast.next.next :
            slow=slow.next
            fast=fast.next.next
        cur=slow.next
        slow.next=None
        prev=None
        while cur: 
            TmpNext=cur.next
            cur.next=prev
            prev=cur
            cur=TmpNext
        first,second=head,prev
        while second :
            temp1=first.next
            temp2=second.next

            first.next=second
            second.next=temp1

            first=temp1
            second=temp2