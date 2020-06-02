class inputValue:
    def inputValueValidation(self) -> int:
          while True:
            try:
                num = int(input("Please input number (-1 to quit) : "))
            except ValueError:
                print("Not an integer! Try again.")  
                continue
            else:
                return num
                break
            
class Solution:
    def numberOfSteps (self, num: int) -> int:
        step = 0
        while num > 1:
            if num % 2 != 0:
                num -= 1
                step += 2
            else:
                step += 1
            num = int(num / 2)
        if(num == 1):
            return step + 1 
        else:
            return step
            
       
        
while True:
    UserInput = inputValue()
    
    num = UserInput.inputValueValidation();
    
    if num == -1:
        break
    
    ansclass = Solution()
    result = ansclass.numberOfSteps(num)
    
    print(result)
