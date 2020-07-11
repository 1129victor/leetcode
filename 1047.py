class Solution:
    def removeDuplicates(self, S: str) -> str:
        import string
        
        dup = {2 * ch for ch in string.ascii_lowercase}
        print(dup)
        prev_length = -1
        while prev_length != len(S):
            prev_length = len(S)
            
            for d in dup:
                S = S.replace(d, '')
            print(S)
        
        return S


        #result = []
        #result.append(S[0])
        #for i in range(1, len(S)):
        #    if result:
        #        temp = result.pop()
        #        if temp != S[i]:
        #            result.append(temp)
        #            result.append(S[i])
        #    else:
        #        result.append(S[i])
        #return ('').join(result)
