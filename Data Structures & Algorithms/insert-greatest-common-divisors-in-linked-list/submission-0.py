# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from math import gcd
class Solution:
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head == None :
            return head
        cur=head
        nex=cur.next
        while nex != None :
            g=gcd(cur.val,nex.val)
            newNode=ListNode(g,nex)
            cur.next=newNode
            cur=nex 
            nex=nex.next
        return head