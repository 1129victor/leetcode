"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def maxDepth(self, root: 'Node') -> int:
        if not root:
            return 0
        
        queueList = [root]
        count = len(queueList)
        childLen = len(queueList)
        
        while queueList:
            temp = queueList.pop(0)
            childLen -= 1
            if temp:
                queueList.extend(temp.children)
            if(childLen == 0 and len(queueList) > 0):
                count += 1
                childLen = len(queueList)
        return count
        
        
