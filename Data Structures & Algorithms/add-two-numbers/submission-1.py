# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        courant1,courant2=l1,l2
        L1,L2=[],[]
        while courant1 and courant2 :
            L1.append(courant1.val)
            L2.append(courant2.val)
            courant1=courant1.next
            courant2=courant2.next
        while courant1 :
            L1.append(courant1.val)
            courant1=courant1.next
        while courant2 :
            L2.append(courant2.val)
            courant2=courant2.next
        r1=int("".join(map(str,reversed(L1))))
        r2=int("".join(map(str,reversed(L2))))
        r=r1+r2
        R=list(str(r))
        R.reverse()
        res=ListNode()
        cur=res
        for i in range(len(R)) :
            cur.val = int(R[i])
            if i == len(R) -1 :
                cur.next=None
            else:
                cur.next = ListNode()
                cur=cur.next
        return res