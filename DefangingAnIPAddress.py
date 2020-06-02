class Solution:
    def defangIPaddr(self, address: str) -> str:
        #print([c if c != '.' else '[.]' for c in address])
        return ''.join([c if c != '.' else '[.]' for c in address])
        
address = "255.100.50.0"
 
ansclass = Solution()
result = ansclass.defangIPaddr(address)

print(result)
