from typing import List
from collections import deque
#from collections import Counter


#create TreeNode class
class TreeNode:
    def __init__(self, val=None, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
    def insert(self, val : int):
        if self.val:
            if self.val > val:
                if self.left is None:
                    self.left = TreeNode(val)
                else:
                    self.left.insert(val)
            elif self.val < val:
                if self.right is None:
                    self.right = TreeNode(val)
                else:
                    self.right.insert(val)
        else:
                self.val = val
                
    
    def printTreeBFS(self):
        print("=============BFS============")
        queue = deque()
        queue.append(self)

        self.recursiveBFS(queue)
        
    def printTreeDFS(self):
        print("=============DFS============")
        stack = []
        stack.append(self)
        self.recursiveDFS(stack)
#        while len(queue) > 0:
#            top = queue.popleft()
#            print(top.val)
#            if top.left is not None:
#                queue.append(top.left)
#                
#            if top.right is not None:
#                queue.append(top.right)
    def recursiveBFS(self, queue):
        if not queue:
            return
        top = queue.popleft()
        print(top.val)
        if top.left is not None:
            queue.append(top.left)
            
        if top.right is not None:
            queue.append(top.right)
        self.recursiveBFS(queue)
        
    def recursiveDFS(self, stack):
        if not stack:
            return    
        top = stack.pop()
        print(top.val)
        if top.right is not None:
            stack.append(top.right)
        
        if top.left is not None:
            stack.append(top.left)
        
        self.recursiveDFS(stack)
        

class inputValue:
    def inputValueValidation(self) -> (List[int], int, int):
          while True:
            try:
                arr1 = list(map(int, input("Please input an array of nums (no input to quit) : ").split()))
                #arr2 = list(map(int, input("Please input an array of index(no input to quit) : ").split()))
                #str1 = str(input("Please input a string (no input to quit) : "))
                num1 = int(input("Please input L integer (-1 to quit) : "))
                num2 = int(input("Please input R integer (-1 to quit) : "))
            except ValueError:
                print("Not an Integer! Try again.")  
                continue
            else:
                return arr1, num1, num2
                break
            
class Solution:
    def rangeSumBST(self, root: TreeNode, L: int, R: int) -> int:
        self.result = 0
        self.dfs(root, L, R)
        return self.result
    
    def dfs(self, root, L, R):
        if not root:
            return
        
        if L <= root.val <= R:
            self.result += root.val
        
        if L <= root.val:
            self.dfs(root.left, L, R)
        
        if root.val <= R:
            self.dfs(root.right, L, R)
        
       
        
while True:
    UserInput = inputValue()
    
    arr1, num1, num2 = UserInput.inputValueValidation();
    
    """
    if num1 == -1:
        break
    """
    
    if len(arr1) == 0 or num1 == -1 or num2 == -1:
        break
    
    ansclass = Solution()
    
    treeNode = TreeNode()   
       
    for i in arr1:
        treeNode.insert(int(i))
            
    result = ansclass.rangeSumBST(treeNode, num1, num2)

    print("ANS :  %d" % result)
    treeNode.printTreeDFS()
    treeNode.printTreeBFS()

