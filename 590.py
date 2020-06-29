"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def postorder(self, root: 'Node') -> List[int]:   
        """
        result = []
        stack = []
        stack.append(root)
        
        while len(stack) > 0 :
            top = stack.pop()
            if top:
                if len(top.children) > 0:
                    temp = top.children
                    top.children = []
                    stack.append(top)
                    for i in temp[::-1]:
                        stack.append(i)

                else:
                    result.append(top.val)
        return result
        """
        if not root: return root
        res = []
        stack = [root]
        while stack:
            temp = stack.pop()
            res.append(temp.val)
            for child in temp.children:
                stack.append(child)
        return res[::-1]
