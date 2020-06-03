from typing import List

#from collections import Counter

class inputValue:
    def inputValueValidation(self) -> (List[int], List[int]):
          while True:
            try:
                arr1 = list(map(int, input("Please input an array of nums (no input to quit) : ").split()))
                arr2 = list(map(int, input("Please input an array of index(no input to quit) : ").split()))
                #num1 = int(input("Please input an integer (-1 to quit) : "))
            except ValueError:
                print("Not a string! Try again.")  
                continue
            else:
                return arr1, arr2
                break
            
class Solution:
    def createTargetArray(self, nums: List[int], index: List[int]) -> List[int]:
        result=[]
        for i in range(len(index)):
            result.insert(index[i], nums[i])
        return result
            
       
        
while True:
    
    UserInput = inputValue()
    
    arr1, arr2 = UserInput.inputValueValidation();
    
    """
    if num1 == -1:
        break
    """
    
    if len(arr1) == 0 or len(arr2) == 0 or len(arr1) != len(arr2):
        break
    
    ansclass = Solution()
    
    result = ansclass.createTargetArray(arr1, arr2)
    
    print(result)
