from typing import List

#from collections import Counter

class inputValue:
    def inputValueValidation(self) -> (str):
          while True:
            try:
                #arr1 = list(map(int, input("Please input an array of nums (no input to quit) : ").split()))
                #arr2 = list(map(int, input("Please input an array of index(no input to quit) : ").split()))
                str1 = str(input("Please input a string (no input to quit) : "))
                #num1 = int(input("Please input an integer (-1 to quit) : "))
            except ValueError:
                print("Not a string! Try again.")  
                continue
            else:
                return str1
                break
            
class Solution:
    def balancedStringSplit(self, s: str) -> int:
        count,check = 0, 0

        for i in s:
            if i == 'R':
                check += 1
            else:
                check -=1
            if check == 0:
                count += 1
        return count
            
       
        
while True:
    
    UserInput = inputValue()
    
    str1 = UserInput.inputValueValidation();
    
    """
    if num1 == -1:
        break
    """
    
    if len(str1) == 0:
        break
    
    ansclass = Solution()
    
    result = ansclass.balancedStringSplit(str1)
    
    print(result)
