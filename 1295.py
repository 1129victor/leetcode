# -*- coding: utf-8 -*-
from typing import List

#from collections import Counter

class inputValue:
    def inputValueValidation(self) -> List[int]:
          while True:
            try:
                arr = list(map(int, input("Please input an array (no input to quit) : ").split()))
                #num1 = int(input("Please input an integer (-1 to quit) : "))
            except ValueError:
                print("Not a string! Try again.")  
                continue
            else:
                return arr
                break
            
class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        count=0
        for i in nums:
            if len(str(i)) % 2 == 0:
                count += 1
        return count
            
       
        
while True:

    UserInput = inputValue()
    
    arr = UserInput.inputValueValidation();
    
    
    if len(arr) == 0:
        break
    """
    if num1 == -1:
        break
    """
    
    ansclass = Solution()
    
    result = ansclass.findNumbers(arr)
    
    print(result)
