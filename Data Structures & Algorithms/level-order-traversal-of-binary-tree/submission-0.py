# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        q = deque([[0, root]])
        res = defaultdict(list)
        depth = 0

        while q:
            level, node = q.popleft()
            res[level].append(node.val)

            if node.left:
                q.append([level + 1, node.left])
            if node.right:
                q.append([level + 1, node.right])
            depth = max(depth, level + 1)

        return [res[i] for i in range(depth)]

