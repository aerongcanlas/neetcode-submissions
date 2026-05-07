# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def dfs(self, node):
        if not node:
            return [True, 0]

        l, r = self.dfs(node.left), self.dfs(node.right)
        isBalanced = l[0] and r[0] and abs(l[1] - r[1]) <= 1

        return [isBalanced, 1 + max(l[1], r[1])]
        

    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        return self.dfs(root)[0]