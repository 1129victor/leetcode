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
    def maxProduct(self, nums: List[int]) -> int:
        sortedNum = sorted(nums)
        return (sortedNum[-1] - 1) * (sortedNum[-2] - 1)
            
       
        
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
    
    result = ansclass.maxProduct(arr)
    
    print(result)
