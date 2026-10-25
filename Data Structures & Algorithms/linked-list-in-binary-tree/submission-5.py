class Solution:
    def isSubPath(self, head: Optional[ListNode], root: Optional[TreeNode]) -> bool:
        L=[]
        def dfs_find(node, val):
            stack = [node]

            while stack:
                curr = stack.pop()

                if not curr:
                    continue

                if curr.val == val:
                    L.append(curr)

                stack.append(curr.right)
                stack.append(curr.left)
        def check(node,cur):
            if not cur :
                return True
            if not node :
                return False
            if node.left and node.left.val == cur.val:
                if check(node.left,cur.next):
                    return True
            if node.right and node.right.val==cur.val:
                return check(node.right,cur.next)
        dfs_find(root,head.val)
        if len(L)==0:
            return False
        for node in L:
            if check(node,head.next):
                return True
        return False
