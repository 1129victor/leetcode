# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

from typing import List

from collections import Counter

class inputValue:
    def inputValueValidation(self) -> List[int]:
          while True:
            try:
                arr = list(map(int, input("Please input an array (no input to quit) : ").split()))
            except ValueError:
                print("Not a string! Try again.")  
                continue
            else:
                return arr
                break
            
class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        sortedNums = sorted(nums)
        Dict = {}
        for i in range(len(nums)):
            if sortedNums[i] not in Dict:
                Dict[sortedNums[i]] = i
        result = []
        for i in range(len(nums)):
            result.append(Dict[nums[i]])
        return result
            
       
        
while True:
    
    UserInput = inputValue()
    
    arr = UserInput.inputValueValidation();
    
    if len(arr) == 0:
        break
    
    
    
    ansclass = Solution()
    
    result = ansclass.smallerNumbersThanCurrent(arr)
    
    print(result)
