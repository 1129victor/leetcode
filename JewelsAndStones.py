from collections import Counter

class inputValue:
    def inputValueValidation(self) -> (str, str):
          while True:
            try:
                str1 = str(input("Please input jewel (-1 to quit) : "))
                str2 = str(input("Please input stone (-1 to quit) : "))
            except ValueError:
                print("Not a string! Try again.")  
                continue
            else:
                return str1, str2
                break
            
class Solution:
    def numJewelsInStones(self, J: str, S: str) -> int:
        result = 0
        counts = Counter(S)
        for c in counts:
            if c in J:
                result += counts[c]
        return result
            
       
        
while True:
    UserInput = inputValue()
    
    str1, str2 = UserInput.inputValueValidation();
    
    if str1 == "-1" or str2 == "-1":
        break
    
    ansclass = Solution()
    
    result = ansclass.numJewelsInStones(str1, str2)
    
    print(result)
