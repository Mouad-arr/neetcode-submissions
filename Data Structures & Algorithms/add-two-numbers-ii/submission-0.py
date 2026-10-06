# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        str1,str2="",""
        cur=l1
        while cur :
            str1 += str(cur.val)
            cur = cur.next
        cur=l2
        while cur : 
            str2 += str(cur.val)
            cur = cur.next
        n1,n2=int(str1),int(str2)
        n=n1+n2
        s=str(n)
        dummy = ListNode()
        cur = dummy

        for digit in s:
            cur.next = ListNode(int(digit))
            cur = cur.next

        return dummy.next