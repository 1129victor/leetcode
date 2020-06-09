from typing import List
 
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
 
class LinkedList:
    def __init__(self):
        self.head=None
    def insert(self, val: int):
        if not self.head:
            self.head = ListNode(val)
        else:  
            temp = self.head
            while temp.next:
                temp = temp.next
            temp.next = ListNode(val)
     
    def reverseRecursive(self, current, previous): 
        if current.next is None : 
            self.head = current   
            current.next = previous 
            return 
        next = current.next
        current.next = previous  
        self.reverseRecursive(next, current)  
    def reverse2(self): 
        if self.head is None: 
            return 
        self.reverseRecursive(self.head, None)         
     
 
 
    def reverse(self):
        if not self:
            return
 
        previous = ListNode(None)
        current = self.head
        preceding = self.head.next
     
        while preceding is not None:
            current.next = previous
            previous = current
            current = preceding
            preceding = preceding.next
         
        current.next = previous
        self.head = current
      
    def printList(self):
        temp = self.head
     
        while temp:
            print(temp.val)
            temp = temp.next
     
 
class inputValue:
    def inputValueValidation(self) -> List[int]:
        while True:
            try:
                arr1 = list(map(int, input("Please input an array of nums (no input to quit) : ").split()))
                #arr2 = list(map(int, input("Please input an array of index(no input to quit) : ").split()))
                #str1 = str(input("Please input a string (no input to quit) : "))
                #num1 = int(input("Please input L integer (-1 to quit) : "))
                #num2 = int(input("Please input R integer (-1 to quit) : "))
            except ValueError:
                print("Not an Integer! Try again.")  
                continue
            else:
                return arr1
                break
 
class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        result = 0
        while head:
            result = result << 1 | head.val
            head = head.next
        return result
 

 
while True:
    UserInput = inputValue()
 
    arr1 = UserInput.inputValueValidation()
     
    """
    if num1 == -1:
    break
    """
     
    if len(arr1) == 0:
        break
    
    ansclass = Solution()
       
    linkedList = LinkedList()
    
    for i in arr1:
        linkedList.insert(i)
         
    result = ansclass.getDecimalValue(linkedList.head)
     
    print("ANS :  %d" % result)
    #print("===========print List Node===============")
    #linkedList.printList()
    #listNode = listNode.reverse()
    #linkedList.reverse()
    #print("===========print reverse Node===============")
    #linkedList.printList()
 
    

