# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        left, right = p, q
        if right.val < left.val:
            left, right = right, left
        if p.val == root.val or q.val == root.val or left.val < root.val < right.val:
            return root
        
        if left.val < root.val and right.val < root.val:
            return self.lowestCommonAncestor(root.left, p, q)
        else:
            return self.lowestCommonAncestor(root.right, p, q)
        # p <= curnode <= q given p < q return curnode
        # p or q == curnode return curnode
        # p and q < curnode go left
        # p and q > curnode go right