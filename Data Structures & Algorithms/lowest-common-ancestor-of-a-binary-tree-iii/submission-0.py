"""
# Definition for a Node.
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.parent = None
"""

class Solution:
    def lowestCommonAncestor(self, p: 'Node', q: 'Node') -> 'Node':
        parents={p,q}
        cur1=p
        cur2=q
        while cur1 and cur2 :
            if cur1.parent in parents:
                return cur1.parent
            else:
                parents.add(cur1.parent)
            cur1=cur1.parent
            if cur2.parent in parents:
                return cur2.parent
            else:
                parents.add(cur2.parent)
            cur2=cur2.parent
        while cur1 :
            if cur1.parent in parents:
                return cur1.parent
            else:
                parents.add(cur1.parent)
            cur1=cur1.parent
        while cur2 :
            if cur2.parent in parents:
                return cur2.parent
            else:
                parents.add(cur2.parent)
            cur2=cur2.parent
        return None