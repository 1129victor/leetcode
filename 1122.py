class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        #result = []
        #for i in arr2:
        #    while i in arr1:
        #        result.append(i)
        #        arr1.remove(i)
        #if arr1:
        #    arr1 = sorted(arr1)
        #    result.extend(arr1)
        #return result
    
        res, cnt = [], Counter(arr1)
        for i in arr2:
            res.extend([i] * cnt.pop(i))
        
        res.extend(sorted(cnt.elements()))
        return res
