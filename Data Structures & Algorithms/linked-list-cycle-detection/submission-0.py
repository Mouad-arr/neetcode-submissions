# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        courant=head 
        index=-1
        List=[]
        while index == -1 and courant is not None :
            if courant not in List :
                List.append(courant)
                courant=courant.next
            else :
                index=1
        if index==-1 :
            return False
        else :
            return True