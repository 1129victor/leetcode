# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
'''
result = 0
def inorderRec(pathStack, tree):
    if not tree:
        return
    pathStack.append(tree.val)
    
    if not tree.left and not tree.right:
        s = [str(i) for i in pathStack]
        tempBin = ('').join(s)
        print(tempBin)
        global result
        result += int(tempBin, 2)
        
    if tree.left:
        inorderRec(pathStack, tree.left)
    if tree.right:
        inorderRec(pathStack, tree.right)
    pathStack.pop()
'''
class Solution:
    def sumRootToLeaf(self, root: TreeNode, val = 0) -> int:
        '''
        pathStack = []
        inorderRec(pathStack, root)
        global result
        ans = result
        result = 0
        return ans
        '''
        if not root:
            return 0
        def helper(root, acc):
            if not root:
                return 0
            acc <<= 1
            acc |= root.val
            if not root.left and not root.right:
                return acc
            return helper(root.left, acc) + helper(root.right, acc)
        return helper(root, 0)
