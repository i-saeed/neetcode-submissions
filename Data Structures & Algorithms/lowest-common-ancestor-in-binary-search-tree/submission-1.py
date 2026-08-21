# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

def smallestPathBST(root: TreeNode, target: TreeNode) -> list[int]:
    path = [0]
    node = root

    while True:
        if node.val == target.val:
            break
        elif target.val > node.val:
            node = node.right
            path.append(1)
        else:
            node = node.left
            path.append(-1)

    return path

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        p_path = smallestPathBST(root, p)
        q_path = smallestPathBST(root, q)
        ancestor = root
        i = 1
        node = root
        while i < min(len(p_path), len(q_path)):
            if p_path[i] != q_path[i]:
                break

            if p_path[i] == -1:
                node = node.left
            else:
                node = node.right

            ancestor = node

            i += 1

        return ancestor    