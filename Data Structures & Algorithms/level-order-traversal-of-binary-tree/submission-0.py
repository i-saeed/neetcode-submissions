# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        traversal = []
        if root is None:
            return traversal

        que = deque([root])
        while que:
            level = len(que)
            traversalLevel = []
            for i in range(level):
                node = que.popleft()
                traversalLevel.append(node.val)
                if node.left is not None:
                    que.append(node.left)
                if node.right is not None:
                    que.append(node.right)
            traversal.append(traversalLevel)
        return traversal      