# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        #depth = 0
        def inorder(root, depth):
            if not root:
                return 0
            depth += 1
            if not root.left and not root.right:
                return depth
            return max(inorder(root.left, depth), inorder(root.right, depth))
        return inorder(root, 0)
