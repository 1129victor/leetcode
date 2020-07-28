'''
def merge(list1, list2):  
    merged_list = [(p1, p2) for idx1, p1 in enumerate(list1)  
        for idx2, p2 in enumerate(list2) if idx1 == idx2] 
    return merged_list 
'''
class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        '''
        sList = list(s)
        result = ''
        stuple = merge(indices, sList)
        print(stuple)
        stuple.sort()
        for i, j in stuple:
            result += j
        return result
        '''
        a=['0']*len(s)
        for i in range(len(s)):
            a[indices[i]]=s[i]
        return "".join(a)
