# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

def isValidBSTNode(
    node: Optional[TreeNode],
    min_val: Optional[int] = None,
    max_val: Optional[int] = None,
) -> bool:
    if node is None:
        return True
    if (min_val is not None and node.val <= min_val) or (
        max_val is not None and node.val >= max_val
    ):
        return False

    return isValidBSTNode(node.left, min_val, node.val) and isValidBSTNode(
        node.right, node.val, max_val
    )

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        return isValidBSTNode(root)