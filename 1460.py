from typing import List

#from collections import Counter

class inputValue:
    def inputValueValidation(self) -> (List[int], List[int]):
          while True:
            try:
                arr1 = list(map(int, input("Please input an array of nums (no input to quit) : ").split()))
                arr2 = list(map(int, input("Please input an array of index(no input to quit) : ").split()))
                #str1 = str(input("Please input a string (no input to quit) : "))
                #num1 = int(input("Please input an integer (-1 to quit) : "))
            except ValueError:
                print("Not a string! Try again.")  
                continue
            else:
                return arr1, arr2
                break
            
class Solution:
    def canBeEqual(self, target: List[int], arr: List[int]) -> bool:
        target.sort()
        arr.sort()
        return target == arr
        
       
        
while True:
    
    UserInput = inputValue()
    
    arr1, arr2 = UserInput.inputValueValidation();
    
    """
    if num1 == -1:
        break
    """
    
    if len(arr1) == 0 or len(arr2) == 0:
        break
    
    ansclass = Solution()
    
    result = ansclass.canBeEqual(arr1, arr2)
    
    print(result)
