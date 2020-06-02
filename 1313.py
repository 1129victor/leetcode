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
    def decompressRLElist(self, nums: List[int]) -> List[int]:
        ans = []
        for i in range(0, len(nums), 2):
            ans.extend([nums[i+1]] * nums[i])
        return ans
            
       
        
while True:
    
    UserInput = inputValue()
    
    arr = UserInput.inputValueValidation();
    
    
    if len(arr) % 2 != 0 or len(arr) == 0:
        break
    """
    if num1 == -1:
        break
    """
    
    ansclass = Solution()
    
    result = ansclass.decompressRLElist(arr)
    
    print(result)
