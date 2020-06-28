"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        temp = []
        result = []
        
        temp.append(root)
        
        while len(temp) > 0:
            now = temp.pop()
            if now:
                now.children.reverse()
                temp.extend(now.children)
                result.append(now.val)
        
        return result
