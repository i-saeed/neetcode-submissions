# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

def DFSInorder(node: Optional[TreeNode], traversal: list[int]) -> None:
    if node is None:
        return

    DFSInorder(node.left, traversal)
    traversal.append(node.val)
    DFSInorder(node.right, traversal)

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        traversed = []
        DFSInorder(root, traversed)
        if k > len(traversed):
            return -1000000
        return traversed[k - 1]        