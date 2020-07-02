# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

def inOrder(result:TreeNode, root:TreeNode):
    if root.left:
        inOrder(result, root.left)

    temp = result
    while temp.right:
        temp = temp.right
    temp.right = TreeNode(root.val)
        
    
    if root.right:
        inOrder(result, root.right)


class Solution:
    def increasingBST(self, root: TreeNode) -> TreeNode:
        if not root:
            return null
        result = TreeNode()
        inOrder(result, root)
        return result.right
