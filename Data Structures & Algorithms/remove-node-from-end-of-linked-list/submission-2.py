# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if not head :
            return 
        arr=[]
        courant=head
        while courant :
            arr.append(courant)
            courant=courant.next
        target=len(arr)-n
        if target == 0 :
            return head.next
        res=ListNode()
        cour=res
        for i in range(len(arr)) :
            if i == target :
                cour.next=None
                continue
            else :
                cour.next=arr[i]
                cour=cour.next
        return res.next