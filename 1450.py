from typing import List

#from collections import Counter

class inputValue:
    def inputValueValidation(self) -> (List[int], List[int], int):
          while True:
            try:
                arr1 = list(map(int, input("Please input an array of nums (no input to quit) : ").split()))
                arr2 = list(map(int, input("Please input an array of index(no input to quit) : ").split()))
                #str1 = str(input("Please input a string (no input to quit) : "))
                num1 = int(input("Please input an integer (-1 to quit) : "))
            except ValueError:
                print("Not a string! Try again.")  
                continue
            else:
                return arr1, arr2, num1
                break
            
class Solution:
    def busyStudent(self, startTime: List[int], endTime: List[int], queryTime: int) -> int:
        count = 0
        for i in range(len(startTime)):
            if startTime[i] <= queryTime and endTime[i] >= queryTime:
                count += 1
        return count
            
       
        
while True:
    
    UserInput = inputValue()
    
    arr1, arr2, num1 = UserInput.inputValueValidation();
    
    """
    if num1 == -1:
        break
    """
    
    if len(arr1) == 0 or len(arr2) == 0 or num1 == -1 or len(arr1) != len(arr2):
        break
    
    ansclass = Solution()
    
    result = ansclass.busyStudent(arr1, arr2, num1)
    
    print(result)
