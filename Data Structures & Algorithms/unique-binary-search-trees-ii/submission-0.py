class Solution:
    def generateTrees(self, n: int) -> List[TreeNode]:

        def construct(start, end):
            res = []

            if start > end:
                return [None]

            for i in range(start, end + 1):

                lefts = construct(start, i - 1)
                rights = construct(i + 1, end)

                for left in lefts:
                    for right in rights:
                        root = TreeNode(i)
                        root.left = left
                        root.right = right
                        res.append(root)

            return res

        return construct(1, n)