from typing import List

#from collections import Counter

class inputValue:
    def inputValueValidation(self) -> int:
          while True:
            try:
                #arr = list(map(int, input("Please input an array (no input to quit) : ").split()))
                num1 = int(input("Please input an integer (-1 to quit) : "))
            except ValueError:
                print("Not a string! Try again.")  
                continue
            else:
                return num1
                break
            
class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        product = 1
        sum1 = 0
        for c in str(n):
            product *= int(c)
            sum1 += int(c)
        return product - sum1
            
       
        
while True:
    
    UserInput = inputValue()
    
    num1 = UserInput.inputValueValidation();
    
    
    if num1 == -1:
        break
    
    
    ansclass = Solution()
    
    result = ansclass.subtractProductAndSum(num1)
    
    print(result)
